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

        const card = document.getElementById("post")

        console.log(result.data)
        result.data.forEach(post => {
            const card = document.createElement("div");
            card.className = "cardExplore";

            card.innerHTML = `
                <h4>${post.title}</h4>
                <p>${post.recipe}</p>
            `;

            postSection.appendChild(card);
        });

    } catch (err) {
        console.error("Failed to load posts", err);
        postSection.in
    }
});