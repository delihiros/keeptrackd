import sqlite3

from keeptrackd import (
        config
        )


class DBManager:
    def __init__(self):
        self.connection = sqlite3.connect(config.get('database_filename'))
        self.cursor = self.connection.cursor()
        query = 'create table if not exists keeptrackd (url text primary key, value text)'
        self.cursor.execute(query)

    def __del__(self):
        self.connection.close()

    def _execute(self, query):
        self.cursor.execute(query)

    def _commit(self):
        self.connection.commit()

    def save(self, url, value):
        query = "replace into keeptrackd (url, value) values (?, ?)"
        self.cursor.execute(query, (str(url), str(value)))
        self._commit()

    def get(self, url):
        query = "select * from keeptrackd where url = ?"
        self.cursor.execute(query, (str(url), ))
        result = self.cursor.fetchone()
        return result

    def remove(self, url):
        query = "delete from keeptrackd where url = ?"
        self.cursor.execute(query, (str(url), ))
        self._commit()

    def get_all(self):
        query = "select * from keeptrackd"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result