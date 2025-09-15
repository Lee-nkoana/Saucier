// Select all elements with .animate
const animatedElements = document.querySelectorAll(".animate");

const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show"); // add active class
            obs.unobserve(entry.target); // play only once
        }
    });
});

// Observe each element
animatedElements.forEach(el => observer.observe(el));
