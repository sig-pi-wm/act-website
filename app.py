from flask import Flask, render_template, request, redirect, url_for
import helpers as helpers
from dao import DAO

app = Flask(__name__)
dao = DAO()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request)
        return redirect(url_for('data'))
    return render_template('index.html')


@app.route('/data', methods=["GET"])
def data():
    season = request.args.get("season")
    if season is None:
        season = "Fall 2024"
    seasons = ["Fall 2024", "Spring 2023", "Fall 2023"] 
    data = dao.fetch_acts(season)
    return render_template('data.html', seasons=seasons, data=data, season=season)


@app.route('/input', methods=["GET", "POST"])
def input():
    act_data = helpers.get_cleared_act_form_data() 
    characters = [c["character_name"] for c in dao.get_characters()]
    usernames = [u["username"] for u in dao.get_usernames()]
    if request.method == 'POST':
        # check that all fields are full
        # try to upload to db
        # if success, redirect to /data (where the ACT will now show up)
        # else, redirect to form WITH DATA FILLED IN
        act_data["date"] = request.form.get("act-date")
        map_ids = helpers.fill_map_ids(request.form.get("top-or-bottom-cups"))
        for i in range(4):
            act_data["teams"][i]["score"] = request.form.get(f"t{i}-total-score")
            act_data["teams"][i]["character"] = request.form.get(f"t{i}-character-select")
            team_user_ids = dao.get_team_user_ids([request.form.get(f"t{i}-p{j}-username-select") for j in range(1,3)])
            act_data["teams"][i]["players"] = [{"user_id": user_id} for user_id in team_user_ids]
        for i in range(16):
            act_data["races"][i]["map_id"] = map_ids[i]
            # for j in range(4):
                # box = request.form.get()
                # act_data["races"][i]["players"][j]["user_id"] = 
                # act_data["races"][i]["players"][j]["points"]

        test_data = act_data
    else:
        test_data = "this was a GET"

    return render_template('input.html', usernames=usernames, characters=characters, act_data=act_data, test_data=test_data)


if __name__ == '__main__':
    app.run(debug=True)
