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

@app.route('/data', methods=["GET", "POST"])
def data():
    if request.method == 'POST':
        season = request.form.get("season")
    else:
        season = "Fall 2024"
    print(season)
    
    #TODO fetch both from DB
    seasons = ["Fall 2024", "Spring 2023", "Fall 2023"] 
    data = [
        season + " Data...",
        "ACT 1",
        "ACT 2",
        "ACT 3",
        "ACT 4",
    ]
    return render_template('data.html', seasons=seasons, data=data)

if __name__ == "__main__":
    app.run(debug=True)
