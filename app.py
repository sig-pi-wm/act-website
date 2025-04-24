from flask import Flask, render_template, request, redirect, url_for
from database.manipulation import Client 

app = Flask(__name__)
db = Client(app)

@app.route('/', methods=["GET"])
def index():
    db.test()
    return render_template('index.html')


#@app.route('/data', methods=["GET"])
#def data():
#    season = request.args.get("season")
#    if season is None:
#        season = "Fall 2024"
#    seasons = ["Fall 2024", "Spring 2024", "Fall 2023", "Spring 2023", "Fall 2022"] 
#    data = dao.fetch_acts(season)
#    return render_template('data.html', seasons=seasons, data=data, season=season)


# @app.route('/input', methods=["GET", "POST"])
# def input():
#     characters = [c["character_name"] for c in dao.get_characters()]
#     usernames = [u["username"] for u in dao.get_usernames()]
#     if request.method == 'POST':
#         body = request.json
#         dao.enter_ACT_from_json(body)
#         return redirect(url_for("input"))

#     return render_template('input.html', usernames=usernames, characters=characters)


# @app.route('/add-username', methods=["GET", "POST"])
# def add_username():
#     if request.method == 'POST':
#         username = request.form.get("username")
#         dao.add_username(username)
#     return render_template('add-username.html')


#@app.route('/leaderboard', methods=["GET"])
#def leaderboard():
#    users = dao.get_all_users_for_leaderboard()
#    return render_template('leaderboard.html', users=users)
#
#@app.route('/sat', methods=["GET"])
#def sat():
#    return render_template('sat.html')
        

if __name__ == '__main__':
    app.run(debug=True)
