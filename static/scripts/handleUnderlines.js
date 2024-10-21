const underlineClickables = document.getElementsByClassName("clickable-underline");
for (let underlineElement of underlineClickables) {
    underlineElement.addEventListener('click', (event) => {
        let underline = event.currentTarget;
        let hiddenInput = underline.getElementsByClassName("underline-hidden-input")[0];
        let teamNumber = hiddenInput.getAttribute("value");

        if (teamNumber == "1") {
            hiddenInput.value = "2";
            underline.classList.toggle('player-2');
        } else {
            hiddenInput.value = "1";
            underline.classList.toggle('player-2');
        }
    });
}
