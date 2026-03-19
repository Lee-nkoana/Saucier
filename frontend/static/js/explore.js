document.addEventListener('DOMContentLoaded', async () => {
    const res = await fetch("/api/auth/me", { credentials: "include" });
    if (!res.ok) {
        window.location.href = "/login";
        return;
    }
    const user = await res.json();

    document.getElementById("username").textContent = `Hi ${user.username}`;

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

            btnSave.addEventListener('click', () => {
                try {
                     
                } catch (error) {
                    console.log("Could not save post")
                }
            } )

            card.innerHTML = `
                <h4>${post.title}</h4>
                <p>${post.recipe}</p>
    
            `;

            card.appendChild(btnSave);

            postSection.appendChild(card);
        });

    } catch (err) {
        console.error("Failed to load posts", err);
    }
});