import os
import sqlite3

from items import Login


class Database:
    def __init__(self):
        self.__wd = os.getcwd()
        self.__con = sqlite3.connect(f'{self.__wd}/data.db')
        self.__cur = self.__con.cursor()
        self.__cur.execute("""CREATE TABLE IF NOT EXISTS logins
        (id INTEGER PRIMARY KEY ON CONFLICT REPLACE AUTOINCREMENT NOT NULL, 
        name STRING, username STRING, password STRING);""")
        self.__con.commit()

    def add_login(self, login: Login):
        self.__cur.execute("INSERT INTO logins VALUES(?, ?, ?, ?);", (None, login.name, login.username, login.password))
        self.__con.commit()

    def get_logins(self):
        a = self.__cur.execute("SELECT * FROM logins;").fetchall()
        logins = []
        for i in a:
            logins.append(Login(i[0], str(i[1]), str(i[2]), str(i[3])))
        return logins

    def delete_login(self, login: Login):
        self.__cur.execute(f"DELETE FROM logins WHERE id = '{login.id}';")
        self.__con.commit()
