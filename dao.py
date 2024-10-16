import mysql.connector
import config as config
import os
import glob
import json

class DAO:

    def __init__(self):
        # Get the list of all files in the folder and sort them alphabetically
        files = sorted(glob.glob(os.path.join(config.database_dir, '*')))

        for file in files:
            with open(file, 'r') as f:
                content = f.read()
                statements = content.split(';')
                for statement in statements:
                    self.__do_query(statement)
    

    def __do_query(self, query, values = None):
        cnx = mysql.connector.connect(
            user=config.user,
            password=config.password,
            host=config.host,
            database=config.database,
        )
        cursor = cnx.cursor(dictionary=True)
        query = query.strip()
        if query.endswith(';'):
            query = query[:-1]
        if query == '': # empty
            cnx.close()
            return
        try:
            if values is None:
                cursor.execute(query)
            else:
                cursor.execute(query, values)
            result = cursor.fetchall()
            cnx.commit()
            cnx.close()
            return [row for row in result]
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))
            cnx.close()
    

    def __get_dates_for_season(self, season):
        season_list = season.split()
        season = season_list[0]
        year = season_list[1]

        if season == "Fall":
            start = year + "-06-01"
            end = year + "-12-31"
        elif season == "Spring":
            start = year + "-01-01"
            end = year + "-05-31"
        else:
            print("Malformed season; returning for calendar year")
            start = year + "-01-01"
            end = year + "-12-31"

        return start, end

    
    def __calculate_scores(self, races):
        # populate list in R->L, T->B order of the bottom-right scores
        scores = []
        for j in [4, 8, 12, 16]:
            for team_index in range(1, 5):
                scores.append(sum([race[f"t{team_index}_points"] for race in races[:j]]))
        return scores


    def fetch_acts(self, season):
        query = '''
            SELECT act_id, act_date,
                t1_score, t2_score, t3_score, t4_score,
                t1_character, t2_character, t3_character, t4_character, 
                t1_p1_uid, t1_p2_uid, t1_p3_uid, t1_p4_uid,
                t2_p1_uid, t2_p2_uid, t2_p3_uid, t2_p4_uid,
                t3_p1_uid, t3_p2_uid, t3_p3_uid, t3_p4_uid,
                t4_p1_uid, t4_p2_uid, t4_p3_uid, t4_p4_uid,
                (SELECT username FROM users WHERE user_id = t1_p1_uid) AS "t1_p1_uname",
                (SELECT username FROM users WHERE user_id = t1_p2_uid) AS "t1_p2_uname",
                (SELECT username FROM users WHERE user_id = t1_p3_uid) AS "t1_p3_uname",
                (SELECT username FROM users WHERE user_id = t1_p4_uid) AS "t1_p4_uname",
                (SELECT username FROM users WHERE user_id = t2_p1_uid) AS "t2_p1_uname",
                (SELECT username FROM users WHERE user_id = t2_p2_uid) AS "t2_p2_uname",
                (SELECT username FROM users WHERE user_id = t2_p3_uid) AS "t2_p3_uname",
                (SELECT username FROM users WHERE user_id = t2_p4_uid) AS "t2_p4_uname",
                (SELECT username FROM users WHERE user_id = t3_p1_uid) AS "t3_p1_uname",
                (SELECT username FROM users WHERE user_id = t3_p2_uid) AS "t3_p2_uname",
                (SELECT username FROM users WHERE user_id = t3_p3_uid) AS "t3_p3_uname",
                (SELECT username FROM users WHERE user_id = t3_p4_uid) AS "t3_p4_uname",
                (SELECT username FROM users WHERE user_id = t4_p1_uid) AS "t4_p1_uname",
                (SELECT username FROM users WHERE user_id = t4_p2_uid) AS "t4_p2_uname",
                (SELECT username FROM users WHERE user_id = t4_p3_uid) AS "t4_p3_uname",
                (SELECT username FROM users WHERE user_id = t4_p4_uid) AS "t4_p4_uname"
            FROM acts
            WHERE act_date BETWEEN %s AND %s;
        '''
        acts_data = self.__do_query(query, values=self.__get_dates_for_season(season))

        query = '''
            SELECT 
                race_id,
                act_id,
                map_id, map_name, cup,
                race_number,
                t1_player_uid, t2_player_uid, t3_player_uid, t4_player_uid,
                t1_points, t2_points, t3_points, t4_points
            FROM races LEFT JOIN maps USING (map_id)
            WHERE act_id = %s
            ORDER BY race_id
        '''
        acts = []

        for act_data in acts_data:
            act_id = act_data["act_id"]
            races = self.__do_query(query, values=[act_id])
            scores = self.__calculate_scores(races)
            act = {
                "data": act_data,
                "races": races,
                "scores": scores
            }
            acts.append(act)

        return acts


    def enter_ACT(self, data):
        cnx = mysql.connector.connect(
            user=config.user,
            password=config.password,
            host=config.host,
            database=config.database,
        )
        cursor = cnx.cursor(dictionary=True)

        date = data["date"]

        t1_score = data["teams"][0]["score"]
        t2_score = data["teams"][1]["score"]
        t3_score = data["teams"][2]["score"]
        t4_score = data["teams"][3]["score"]

        t1_character = data["teams"][0]["character"]
        t2_character = data["teams"][1]["character"]
        t3_character = data["teams"][2]["character"]
        t4_character = data["teams"][3]["character"]

        t1_p1_uid = data["teams"][0]["players"][0]["user_id"]
        t1_p2_uid = data["teams"][0]["players"][1]["user_id"]
        t1_p3_uid = data["teams"][0]["players"][2]["user_id"]
        t1_p4_uid = data["teams"][0]["players"][3]["user_id"]

        t2_p1_uid = data["teams"][1]["players"][0]["user_id"]
        t2_p2_uid = data["teams"][1]["players"][1]["user_id"]
        t2_p3_uid = data["teams"][1]["players"][2]["user_id"]
        t2_p4_uid = data["teams"][1]["players"][3]["user_id"]

        t3_p1_uid = data["teams"][2]["players"][0]["user_id"]
        t3_p2_uid = data["teams"][2]["players"][1]["user_id"]
        t3_p3_uid = data["teams"][2]["players"][2]["user_id"]
        t3_p4_uid = data["teams"][2]["players"][3]["user_id"]

        t4_p1_uid = data["teams"][3]["players"][0]["user_id"]
        t4_p2_uid = data["teams"][3]["players"][1]["user_id"]
        t4_p3_uid = data["teams"][3]["players"][2]["user_id"]
        t4_p4_uid = data["teams"][3]["players"][3]["user_id"]

        query = '''
            INSERT INTO acts (
                act_date,
                t1_score, t2_score, t3_score, t4_score,
                t1_character, t2_character, t3_character, t4_character, 
                t1_p1_uid, t1_p2_uid, t1_p3_uid, t1_p4_uid,
                t2_p1_uid, t2_p2_uid, t2_p3_uid, t2_p4_uid,
                t3_p1_uid, t3_p2_uid, t3_p3_uid, t3_p4_uid,
                t4_p1_uid, t4_p2_uid, t4_p3_uid, t4_p4_uid
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        values = (
            date, 
            t1_score, t2_score, t3_score, t4_score,
            t1_character, t2_character, t3_character, t4_character, 
            t1_p1_uid, t1_p2_uid, t1_p3_uid, t1_p4_uid,
            t2_p1_uid, t2_p2_uid, t2_p3_uid, t2_p4_uid,
            t3_p1_uid, t3_p2_uid, t3_p3_uid, t3_p4_uid,
            t4_p1_uid, t4_p2_uid, t4_p3_uid, t4_p4_uid
        )

        try:
            cursor.execute(query, values)
        except mysql.connector.Error as err:
            print("Failed to enter ACT, not attempting to enter races: {}".format(err))
            cnx.rollback()
            cnx.close()
            return

        act_id = cursor.lastrowid
        
        query = '''
            INSERT INTO races (
                act_id,
                map_id,
                race_number,
                t1_player_uid, t2_player_uid, t3_player_uid, t4_player_uid,
                t1_points, t2_points, t3_points, t4_points
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        for race in data["races"]:
            values = (
                act_id,
                race["map_id"],
                race["race_number"],
                race["players"][0]["user_id"], race["players"][1]["user_id"], race["players"][2]["user_id"], race["players"][3]["user_id"],
                race["players"][0]["points"], race["players"][1]["points"], race["players"][2]["points"], race["players"][3]["points"]
            )
            try:
                query = query.strip()
                cursor.execute(query, values)
            except:
                print("A race failed to enter. Rolling back to 0 races entered.")
                cnx.rollback()
                cnx.close()
                return
        cnx.commit()
        cnx.close()


    def enter_test_users(self):
        query = '''INSERT INTO users (username) VALUES (%s)'''
        names = ["bert", "rolf", "eli", "manzari", "justin", "mcguinness", "katabian", "mehler"]
        for name in names:
            self.__do_query(query, [name])
            
# db = DAO()
# with open("example-data.json") as file:
#     data = json.load(file)
# dao.enter_test_users()
# db.enter_ACT(data)
