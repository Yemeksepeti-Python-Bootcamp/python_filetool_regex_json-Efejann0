import sqlite3
from moduless.users_data import User_Datas
from datetime import datetime

timer=datetime.now().strftime('%Y%m%d')

class Database(object):
    def __init__(self, db_path):
        self.db_path = db_path

    def __exit__(self):
        self.cursor.close()
        self.connection.close()
    def create_table(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cur = self.connection.cursor()
        self.cur.execute((f""" CREATE TABLE IF NOT EXISTS dataregex_{timer}(
            username text,
            name_surname text,
            email text,
            emailuserlk text,
            usernamelk text, 
            birth_year text,
            birth_month text,
            birth_day text,
            country text,
            active_passive integer
            )"""))
        self.connection.commit()
        self.__exit__()


    def insert_data(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cur = self.connection.cursor()
        self.cur.execute (f"""INSERT INTO dataregex_{timer}
            VALUES(
                "{User_Datas.username}",
                "{User_Datas.name_surname}",
                "{User_Datas.email}",
                "{User_Datas.emailuserlk}",
                "{User_Datas.usernamelk}",
                "{User_Datas.birth_year}",
                "{User_Datas.birth_day}",
                "{User_Datas.birth_month}",
                "{User_Datas.country}",
                "{User_Datas.active_passive}"
                )""")
        self.__exit__()
