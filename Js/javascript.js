// DOM - Document Object Model
function init() {
    const hamburger = document.querySelector(".hamburger");
    const sideBarCloseButton = document.querySelector(".close-button");
    const sideBarContainer = document.querySelector(".sidebar-container");

    
    const openSideBar = () => {
        sideBarContainer.classList.add("show-sidebar");
    }
    const closeSideBar = () => {
        sideBarContainer.classList.remove("show-sidebar");
    }
    hamburger.addEventListener("click", openSideBar);
    sideBarCloseButton.addEventListener("click", closeSideBar);
}
init();

function navbarCode(){
    const navBarContainer = document.querySelector(".nav-container");
window.addEventListener("scroll", function () {
    const scrollNumber = window.scrollY;
    const targetNumber = window.innerWidth >= 992 ? 70 : 50;
    if (scrollNumber >= targetNumber){
        navBarContainer.classList.add("sticky-nav");
    }
    else{
        navBarContainer.classList.remove("sticky-nav");
    }
})
}
navbarCode();



