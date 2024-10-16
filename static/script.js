const handleSubmit = (e) => {
    e.preventDefault();
    formData = new FormData(e.target);

    for (value of formData.values()) {
        if (value === "") {
            //popup that says form is incomplete
            // specify which thing to fill in based on key
            break;
        }
    }

    const actJson = parseActFormToJson(formData);
    console.log(actJson)
}


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
            const underlinedPlayer = formData.get(`t${j+1}-underline`);
            const isRaceUnderlined = ("on" === formData.get(`t${j+1}-r${i+1}-underline`));
            let playerNumber;
            if (isRaceUnderlined) {
                playerNumber = underlinedPlayer;
            } else {
                if (underlinedPlayer === "1") {
                    playerNumber = 2;
                }
                else {
                    playerNumber = 1;
                }
            }
            
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