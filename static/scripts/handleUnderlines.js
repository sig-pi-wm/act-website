const underlineClickables = document.getElementsByClassName("clickable-underline");
for (let underlineElement of underlineClickables) {
    underlineElement.addEventListener('click', (event) => {
        console.log('click');
        console.log(event.currentTarget);
        let underline = event.currentTarget;
        let hiddenInput = underline.getElementsByClassName("underline-hidden-input")[0];
        console.log(hiddenInput);
        let teamNumber = hiddenInput.getAttribute("value");
        console.log(teamNumber);

        if (teamNumber == "1") {
            hiddenInput.value = "2";
            underline.classList.toggle('team-2');
        } else {
            hiddenInput.value = "1";
            underline.classList.toggle('team-2');
        }
        // let checkbox = event.currentTarget.getElementsByClassName("race-scores-checkbox")[0];
        // console.log(checkbox);
        // console.log(checkbox.value);
        // if (checkbox.checked) {
        //     checkbox.checked = false;
        // } else {
        //     checkbox.checked = true;
        // }
        // console.log(checkbox)
    });
}
