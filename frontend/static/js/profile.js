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

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById("createPostForm").style.display = "none";
})