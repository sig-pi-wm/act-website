const handleClick = () => {
    document.getElementById("sidenav").classList.toggle('collapsed');
    document.getElementById("body-main").classList.toggle('full-width');
};

const hamburgerMenuButton = document.getElementById("hamburger-menu-button");
hamburgerMenuButton.addEventListener('click', handleClick);
