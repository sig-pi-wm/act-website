from flask import Flask, render_template, request, redirect, url_for
import helpers as helpers
from dao import DAO

app = Flask(__name__)
dao = DAO()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
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
    characters = [c["character_name"] for c in dao.get_characters()]
    usernames = [u["username"] for u in dao.get_usernames()]
    if request.method == 'POST':
        body = request.json
        dao.enter_ACT_from_json(body)
        return redirect(url_for("input"))

    return render_template('input.html', usernames=usernames, characters=characters)


if __name__ == '__main__':
    app.run(debug=True)
