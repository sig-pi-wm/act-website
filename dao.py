import mysql.connector
import config as config
import os
import glob
import json
import pprint

class DAO:

    def __init__(self):
        self.__cnx = mysql.connector.connect(
            user=config.user,
            password=config.password,
            host=config.host,
        )
        self.__cursor = self.__cnx.cursor()
        self.__build_from_schema("./database")
    
    def __del__(self):
        self.__cnx.close()

    def __build_from_schema(self, folder_path):
        # Get the list of all files in the folder and sort them alphabetically
        files = sorted(glob.glob(os.path.join(folder_path, '*')))

        for file in files:
            with open(file, 'r') as f:
                print(f"{file}:")
                content = f.read()
                statements = content.split(';')
                for statement in statements:
                    self.__do_query(statement)

    def __do_query(self, query, values = None):
        query = query.strip()
        if query.endswith(';'):
            query = query[:-1]
        if query == '': # empty
            return
        try:
            if values is None:
                self.__cursor.execute(query)
            else:
                self.__cursor.execute(query, values)
            self.__cnx.commit()
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))
    
    def __do_query_nocommit(self, query, values = None):
        query = query.strip()
        if query.endswith(';'):
            query = query[:-1]
        if query == '': # empty
            return
        try:
            if values is None:
                self.__cursor.execute(query)
            else:
                self.__cursor.execute(query, values)
        except mysql.connector.Error as err:
            print("Failed query: {}".format(err))

    def enter_ACT(self, data):
        date = data["date"]

        t1_score = data["teams"][0]["score"]
        t2_score = data["teams"][1]["score"]
        t3_score = data["teams"][2]["score"]
        t4_score = data["teams"][3]["score"]

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
                t1_p1_uid, t1_p2_uid, t1_p3_uid, t1_p4_uid,
                t2_p1_uid, t2_p2_uid, t2_p3_uid, t2_p4_uid,
                t3_p1_uid, t3_p2_uid, t3_p3_uid, t3_p4_uid,
                t4_p1_uid, t4_p2_uid, t4_p3_uid, t4_p4_uid
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        # Execute the query with the values
        values = (
            date, 
            t1_score, t2_score, t3_score, t4_score,
            t1_p1_uid, t1_p2_uid, t1_p3_uid, t1_p4_uid,
            t2_p1_uid, t2_p2_uid, t2_p3_uid, t2_p4_uid,
            t3_p1_uid, t3_p2_uid, t3_p3_uid, t3_p4_uid,
            t4_p1_uid, t4_p2_uid, t4_p3_uid, t4_p4_uid
        )

        try:
            self.__do_query(query, values)
        except:
            print("Failed to initialize ACT in DB. Not entering races.")
            return

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

        act_id = self.__cursor.lastrowid
        
        for race in data["races"]:
            values = (
                act_id,
                race["map_id"],
                race["race_number"],
                race["players"][0]["user_id"], race["players"][1]["user_id"], race["players"][2]["user_id"], race["players"][3]["user_id"],
                race["players"][0]["points"], race["players"][1]["points"], race["players"][2]["points"], race["players"][3]["points"]
            )
            try:
                self.__do_query_nocommit(query, values)
            except:
                print("A race failed to enter. Rolling back to 0 races entered.")
                self.__cnx.rollback()
                return
        
        self.__cnx.commit()

    def enter_test_users(self):
        query = '''INSERT INTO users (username) VALUES (%s)'''
        names = ["bert", "rolf", "eli", "manzari", "justin", "mcguinness", "katabian", "mehler"]
        for name in names:
            self.__do_query(query, [name])
            

dao = DAO()
with open("example-data.json") as file:
    data = json.load(file)
pprint.pp(data)
dao.enter_test_users()
dao.enter_ACT(data)
