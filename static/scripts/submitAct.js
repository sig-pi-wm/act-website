const handleSubmit = (e) => {
    e.preventDefault();
    formData = new FormData(e.target);
    let incomplete = false; // Flag for incomplete form

    // for (const [key, value] of formData.entries()) {
    //     if (value === "") {
    //         incomplete = true;
    //         alert(`Please fill in the ${key} field.`);
    //         break;
    //     }
    // }
    if (incomplete) return; // Stop execution if the form is incomplete

    const actJson = parseActFormToJson(formData);
    console.log(actJson)
    return;

    const url = '/input';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(actJson),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
    })
    .then(data => {
        console.log('Success:', data); // Handle successful response
        // Optionally show a success message or update the UI
    })
    .catch(error => {
        console.error('Error:', error); // Handle errors
        // Optionally show an error message to the user
    });
};


const parseActFormToJson = (formData) => {
    let actJson = {};
    actJson.date = formData.get("act-date");

    actJson.teams = []
    for (let i = 0; i < 4; i++) {
        actJson.teams[i] = {
            "score": formData.get(`t${i+1}-total-score`),
            "character": formData.get(`t${i+1}-character`),
            "players": [],
        }
        for (let j = 0; j < 2; j++) { // hardcoded two players, can change
            actJson.teams[i].players[j] = {
                "username": formData.get(`t${i+1}-p${j+1}-username`),
            }
        }
    }

    const cups = formData.get("top-or-bottom-cups");
    let mapIds = Array.from({ length: 16 }, (_, i) => i + 1); // top cups
    if (cups === "bottom") {
        mapIds = Array.from({ length: 16 }, (_, i) => i + 17);
    }

    actJson.races = []
    for (let i = 0; i < 16; i++) {
        actJson.races[i] = {
            "raceNumber": i+1,
            "mapId": mapIds[i],
            "players": [],
        }
        for (let j = 0; j < 4; j++) {
            // const underlinedPlayer = formData.get(`t${j+1}-underline`);
            const playerNumber = formData.get(`t${j+1}-r${i+1}-underline`);
            console.log(`t${j+1}-p${playerNumber}-username`);
 
            actJson.races[i].players[j] = {
                "username": formData.get(`t${j+1}-p${playerNumber}-username`),
                "points": formData.get(`t${j+1}-r${i+1}-score`),
            }
        }
    }

    return actJson;
}

const inputForm = document.getElementById("act-input-form");
inputForm.addEventListener('submit', handleSubmit);