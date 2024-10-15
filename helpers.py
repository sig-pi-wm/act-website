def get_cleared_act_form_data():
    return {
        "date": None,
        "teams": [
            {
                "score": None,
                "character": None,
                "players": [
                    {
                        "user_id": None,
                    }
                    for _ in range(4)
                ]
            }
            for _ in range(4)
        ],
        "races": [
            {
                "race_number": race_number,
                "map_id": None,
                "players": [
                    {
                        "user_id": None,
                        "points": None,
                    }
                    for _ in range(4)
                ]
            }
            for race_number in range(1,17)
        ],
    }


def fill_map_ids(which_cups):
    if which_cups == "top":
        return [i for i in range(1,17)]
    else: # bottom
        return [i for i in range(17,33)]