from dao import DAO

K = 30

dao = DAO()

races = dao.get_all_races()
users = dao.get_all_users()

# elos = {}
# for user in users:
#     # elos["user_id"] = user["elo"]
#     elos["user_id"] = 1000

# for race in races:
#     avg_elo = sum([race[f"t{i}_player_uid"] for i in range(1,5)]) / 4
#     print(avg_elo)
#     for i in range(1,5):
#         cur_elo = elos[race[f"t{i}_player_uid"]]
#         exp_score = 1 / ( 1 + 10**( ( avg_elo - cur_elo) / 400 ) )
#         real_score = race[f"t{i}_points"]
