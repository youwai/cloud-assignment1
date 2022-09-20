const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const overlay = document.getElementById("overlay");

hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
    overlay.style.display = 'block';

    if (!hamburger.classList.contains('active')){
        overlay.style.display = 'none';
    }
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
    overlay.style.display = 'none';
}))

overlay.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
    overlay.style.display = 'none';
})