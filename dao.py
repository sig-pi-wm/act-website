import mysql.connector
import config as config
import os
import glob

class DAO:

    def __init__(self):
        self.__cnx = mysql.connector.connect(
            user=config.user,
            password=config.password,
            host=config.host,
        )
        self.__build_from_schema("./database")
    
    def __del__(self):
        self.__cnx.close()

    def __build_from_schema(self, folder_path):
        # Get the list of all files in the folder and sort them alphabetically
        files = sorted(glob.glob(os.path.join(folder_path, '*')))
        cursor = self.__cnx.cursor()

        for file in files:
            with open(file, 'r') as f:
                print(f"{file}:")
                content = f.read()
                statements = content.split(';')
                for statement in statements:
                    statement = statement.strip()
                    if statement == '': # empty
                        continue
                    print(statement)
                    try:
                        cursor.execute(statement)
                        self.__cnx.commit()
                    except mysql.connector.Error as err:
                        print("Failed query: {}".format(err))
 
