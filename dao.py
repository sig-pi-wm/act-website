import mysql.connector
import config as config
import os
import glob

class DAO:

    def __init__(self):
        repo_dir = os.path.dirname(os.path.abspath(__file__))
        schema_builder_path = os.path.join(repo_dir + '/database/schema-builder', '*')
        schema_files = sorted(glob.glob(schema_builder_path))

        for file in schema_files:
            with open(file, 'r') as f:
                content = f.read()
                statements = content.split(';')
                for statement in statements:
                    self.__do_query(statement)
    

    def __do_query(self, query, values = None):
        try:
            cnx = mysql.connector.connect(
                user=config.user,
                password=config.password,
                host=config.host,
                database=config.database,
            )
        except Exception as e:
            print("Connection Error:", e)
            print("Reattempting without specifying database")
            # If database is uninitialized, the .connect method fails when specifying it
            cnx = mysql.connector.connect(
                user=config.user,
                password=config.password,
                host=config.host,
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
    

    def get_characters(self):
        # orders by most frequently used characters
        query = '''
            SELECT character_name
            FROM characters
            ORDER BY (
                SELECT COUNT(*)
                FROM acts
                WHERE characters.character_name IN (
                    t1_character, t2_character, t3_character, t4_character
                )
            ) DESC;
        '''

        return self.__do_query(query)
    

    def get_usernames(self):
        query = 'SELECT username FROM users;'
        return self.__do_query(query)


    def get_team_user_ids(self, team_usernames):
        query = 'SELECT user_id FROM users WHERE username = %s'
        return [self.__do_query(query, [username]) for username in team_usernames]


    def enter_ACT_from_json(self, data):
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

        t1_p1_uid = data["teams"][0]["players"][0]["username"]
        t1_p2_uid = data["teams"][0]["players"][1]["username"]
        # t1_p3_uid = data["teams"][0]["players"][2]["username"]
        # t1_p4_uid = data["teams"][0]["players"][3]["username"]

        t2_p1_uid = data["teams"][1]["players"][0]["username"]
        t2_p2_uid = data["teams"][1]["players"][1]["username"]
        # t2_p3_uid = data["teams"][1]["players"][2]["username"]
        # t2_p4_uid = data["teams"][1]["players"][3]["username"]

        t3_p1_uid = data["teams"][2]["players"][0]["username"]
        t3_p2_uid = data["teams"][2]["players"][1]["username"]
        # t3_p3_uid = data["teams"][2]["players"][2]["username"]
        # t3_p4_uid = data["teams"][2]["players"][3]["username"]

        t4_p1_uid = data["teams"][3]["players"][0]["username"]
        t4_p2_uid = data["teams"][3]["players"][1]["username"]
        # t4_p3_uid = data["teams"][3]["players"][2]["username"]
        # t4_p4_uid = data["teams"][3]["players"][3]["username"]

        query = '''
            INSERT INTO acts (
                act_date,
                t1_score, t2_score, t3_score, t4_score,
                t1_character, t2_character, t3_character, t4_character, 
                t1_p1_uid, t1_p2_uid,
                t2_p1_uid, t2_p2_uid,
                t3_p1_uid, t3_p2_uid,
                t4_p1_uid, t4_p2_uid
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s)
            )
        '''

        values = (
            date, 
            t1_score, t2_score, t3_score, t4_score,
            t1_character, t2_character, t3_character, t4_character, 
            t1_p1_uid, t1_p2_uid,
            t2_p1_uid, t2_p2_uid,
            t3_p1_uid, t3_p2_uid,
            t4_p1_uid, t4_p2_uid
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
            VALUES (%s, %s, %s,
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
                (SELECT user_id FROM users WHERE username = %s),
            %s, %s, %s, %s)
        '''

        for race in data["races"]:
            values = (
                act_id,
                race["mapId"],
                race["raceNumber"],
                race["players"][0]["username"], race["players"][1]["username"], race["players"][2]["username"], race["players"][3]["username"],
                race["players"][0]["points"], race["players"][1]["points"], race["players"][2]["points"], race["players"][3]["points"]
            )
            try:
                query = query.strip()
                cursor.execute(query, values)
            except:
                print("A race failed to enter. Canceling ACT entry. ")
                cnx.rollback()
                cnx.close()
                return
        cnx.commit()
        cnx.close()


    def add_username(self, username):
        query = "INSERT IGNORE INTO users (username) VALUES (%s)";
        self.__do_query(query, [username])

    def update_elo(self, user_id, elo):
        query = '''
            UPDATE users
            SET elo = %s
            WHERE user_id = %s
        '''
        self.__do_query(query, [elo, user_id])

    def get_all_races(self):
        # only use points and strength of schedule
        query = '''
            SELECT 
                act_date,
                act_id,
                race_id,
                t1_player_uid,
                t1_points,
                t2_player_uid,
                t2_points,
                t3_player_uid,
                t3_points,
                t4_player_uid,
                t4_points
            FROM races
            LEFT JOIN acts
            USING (act_id)
            ORDER BY act_date, act_id, race_id
        '''
        return self.__do_query(query)

    def get_all_users(self):
        return self.__do_query('SELECT * FROM users')

    def get_all_users_for_leaderboard(self):
        query = '''
            SELECT u.*, 
                (
                    SELECT COUNT(*)
                    FROM acts
                    WHERE t1_p1_uid = u.user_id OR
                            t1_p2_uid = u.user_id OR
                            t1_p3_uid = u.user_id OR
                            t1_p4_uid = u.user_id OR
                            t2_p1_uid = u.user_id OR
                            t2_p2_uid = u.user_id OR
                            t2_p3_uid = u.user_id OR
                            t2_p4_uid = u.user_id OR
                            t3_p1_uid = u.user_id OR
                            t3_p2_uid = u.user_id OR
                            t3_p3_uid = u.user_id OR
                            t3_p4_uid = u.user_id OR
                            t4_p1_uid = u.user_id OR
                            t4_p2_uid = u.user_id OR
                            t4_p3_uid = u.user_id OR
                            t4_p4_uid = u.user_id
                ) AS act_count
            FROM users u
            ORDER BY elo DESC
        '''
        return self.__do_query(query)
    
    def run_sql_script(self, filename):
        with open(os.path.join(config.database_dir + '/scripts/' + filename), 'r') as f:
            content = f.read()
            statements = content.split(';')
            for statement in statements:
                self.__do_query(statement)


    def get_act_by_id(self, act_id):
        query = '''
            SELECT a.act_date, t.team_id, t.team_id, t.team_number, t.team_character, t.score, u.username
            FROM team_players p
            LEFT JOIN users u ON p.player_id = u.user_id
            LEFT JOIN teams t USING (team_id)
            LEFT JOIN acts a USING (act_id)
            WHERE act_id = %s
        '''
        return self.__do_query(query, [act_id])
    
    def get_races_by_act_id(self, act_id):
        query = '''
            SELECT m.map_name, r.race_number, u.username, p.points
            FROM race_players p
            LEFT JOIN users u ON p.player_id = u.user_id
            LEFT JOIN races r USING (race_id)
            LEFT JOIN maps m ON m.map_id = r.map_id
            LEFT JOIN acts a USING (act_id)
            WHERE act_id = %s
        '''
        return self.__do_query(query, [act_id])
