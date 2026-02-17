document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch("/api/auth/me", { credentials: "include" });
    if (!res.ok) {
        window.location.href = "/login";
        return;
    }
    const user = await res.json();

    document.getElementById("username").textContent = `Hi ${user.username}`;

    const postSection = document.getElementById('postSection');

    try {
        const response = await fetch("/api/auth/posts/all", {
            credentials: "include"
        });
        const result = await response.json();

        if (!result.success || result.data.length === 0) {
            postSection.innerHTML = "<p>No posts yet.</p>";
            return;
        }

        // const card = document.getElementById("post")

        console.log(result.data)
        result.data.forEach(post => {
            const card = document.createElement("div");
            card.className = "card";

            card.innerHTML = `
                <h4>${post.title}</h4>
                <p>${post.recipe}</p>
            `;

            postSection.appendChild(card);
        });

        

        function setupPagination(){
                    //pagination
            const cardsPerPage = 3;
            const dataContainer = document.getElementById("dataContainer");
            const pagination = document.getElementById("pagination");
            const prevButton = document.getElementById("prev");
            const nextButton = document.getElementById("next");
            const pageNumbers = document.getElementById("page-numbers");
            const pageLinks = document.querySelectorAll(".page-link");

            const cards = Array.from(dataContainer.getElementsByClassName("card"));
            const totalPages = Math.ceil(cards.length / cardsPerPage);
            let currentPage = 1;

            function displayPage(page){
                const startIndex = (page - 1) * cardsPerPage;
                const endIndex = startIndex + cardsPerPage;
                cards.forEach((c, index) => {
                    if (index >= startIndex && index <endIndex){
                        c.style.display = 'block';
                    } else {
                        c.style.display = 'none';
                    }
                });
            }

            function updatePagination(){
                pageNumbers.textContent = `Page ${currentPage} of ${totalPages}`;
                prevButton.disabled = currentPage === 1;
                nextButton.disabled = currentPage === totalPages;
                pageLinks.forEach((link) => {
                    const page = parseInt(link.getAttribute("data-page"));
                    link.classList.toggle("active", page === currentPage);
                });
            }

            prevButton.addEventListener("click", () => {
                if ( currentPage > 1){
                    currentPage--;
                    displayPage(currentPage);
                    updatePagination();
                }
            });

            nextButton.addEventListener("click", () => {
                if ( currentPage < totalPages ){
                    currentPage++;
                    displayPage(currentPage);
                    updatePagination();
                }
            });

            pageLinks.forEach((link) => { 
                link.addEventListener('click', (e) => { 
                    e.preventDefault(); 
                    const page = parseInt(link.getAttribute('data-page')); 
                    if (page !== currentPage) { 
                        currentPage = page; 
                        displayPage(currentPage); 
                        updatePagination(); 
                    } 
                }); 
            }); 

            displayPage(currentPage);
            updatePagination();
        }
        setupPagination();

    } catch (err) {
        console.error("Failed to load posts", err);
        postSection.in
    }

    

});