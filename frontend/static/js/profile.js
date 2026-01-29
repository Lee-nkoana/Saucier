function openForm() {
    document.getElementById("createPostForm").style.display = "block";
}

function closeForm() {
    document.getElementById("createPostForm").style.display = "none";
}

document.getElementById("createPostForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const user = getCurrentUser()

    data = {
        title: e.target.title.value.trim(),
        author: user.username,
        recipe: e.target.recipe.value.trim()
    }

    try {
        const response = await fetch("/api/auth/posts", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            credentials: "include",
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log(result);

        if (result.success) {
            closeForm();
            console.log("Post created successfully");
            setTimeout(() => {
                window.location.href = "/explore";
            }, 1000);
        } else {
            console.log("Could not create account. Try again!");
        }
    } catch (err) {
        console.error("Registration error:", err);
        console.log("Something went wrong. Please try again later.");
    }
})

document.addEventListener('DOMContentLoaded', async () => {
    document.getElementById("createPostForm").style.display = "none";

    const user = getCurrentUser();
    if (!user) {
        window.location.href = "/login";
        return;
    }

    const postSection = document.getElementById('postSection');
    console.log(user.username)

    try {
        const response = await fetch(`/api/auth/posts/${user.username}`);
        const result = await response.json();

        if (!result.success || result.data.length === 0) {
            postSection.innerHTML = "<p>No posts yet.</p>";
            return;
        }

        const card = document.getElementById("post")

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

    } catch (err) {
        console.error("Failed to load posts", err);
        postSection.in
    }
});