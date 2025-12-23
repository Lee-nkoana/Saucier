document.addEventListener('DOMContentLoaded', () => {
    const user = getCurrentUser()

    if (!user) {
        window.location.href = "/login";
        return;
    }
    document.getElementById("username").textContent = `Hi ${user.username}`;

})