document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch("/api/auth/me", { credentials: "include" });
    if (!res.ok) {
        window.location.href = "/login";
        return;
    }
    const user = await res.json();

    document.getElementById("username").textContent = `Explore`;

    const postSection = document.getElementById('dataContainer');

    try {
        const response = await fetch("/api/auth/posts/all", {
            credentials: "include"
        });
        const result = await response.json();

        if (!result.success || result.data.length === 0) {
            postSection.innerHTML = "<p>No posts yet.</p>";
            return;
        }

        const shuffled = result.data.sort( () => 0.5 - Math.random());
        const randomThree = shuffled.slice(0,3);
        console.log(randomThree)
        randomThree.forEach( post => {
            const card = document.createElement("div");
            const btnSave = document.createElement("button");
            card.className = "cardExplore";
            btnSave.className = "saveRecipe";
            btnSave.textContent = "Save";

            btnSave.addEventListener('click', async () => {
                try {
                    const res = await fetch("/api/posts/save", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        credentials: "include",
                        body: JSON.stringify({
                            post_id: post.post_id
                        })
                    });

                    const data = await res.json();
                    
                    if (res.ok){
                        btnSave.textContent = "Saved";
                        btnSave.disabled = true;
                    }else{
                        console.log(data.message || "Failed to save post");
                    }

                } catch (error) {
                    console.log("Could not save post")
                }
            } )

            const postHeader = document.createElement("div");
            const postBody = document.createElement("div");
            postHeader.className = "postHeader";
            postBody.className = "postBody";

            postHeader.innerHTML = `
                <h4>${post.title}</h4>
            `
            postHeader.appendChild(btnSave);

            postBody.innerHTML = `
                <p>${post.recipe}</p>
            `
            
            card.appendChild(postHeader);
            card.appendChild(postBody);

            postSection.appendChild(card);
        });

    } catch (err) {
        console.error("Failed to load posts", err);
    }
});