from flask import Flask, render_template, request, redirect, url_for
from config import *
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
    if request.method == 'POST': 
        # check that all fields are full
        # try to upload to db
        # if success, redirect to /data (where the ACT will now show up)
        # else, redirect to form WITH DATA FILLED IN
        pass
    else:
        characters = [c["character_name"] for c in dao.get_characters()]
        return render_template('input.html', characters=characters)


if __name__ == '__main__':
    app.run(debug=True)
