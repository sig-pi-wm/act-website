import pprint
from dao import DAO

K = 30

dao = DAO()

races = dao.get_all_races()
users = dao.get_all_users()

elos = {}
unames = {}
for user in users:
    uid = user["user_id"]
    unames[uid] = user["username"]
    elos[uid] = 1500.0
    # elos[uid] = user["elo"]

for race in races:
    avg_elo = sum([elos[race[f"t{i}_player_uid"]] for i in range(1,5)]) / 4.0
    for i in range(1,5):
        uid = race[f"t{i}_player_uid"]
        uname = unames[uid]
        cur_elo = elos[uid]
        exp_score = 3.0 / ( 1 + 10**( ( avg_elo - cur_elo) / 400.0 ) )
        real_score = race[f"t{i}_points"]
        new_elo = cur_elo + K * ( real_score - exp_score )
        elos[uid] = new_elo

for uid, elo in elos.items():
    dao.update_elo(uid, elo)