import os
import sqlite3


class DBConnection:
    db_file = os.path.join(os.environ.get('SQLITE_DB_PATH', os.path.abspath(os.getcwd())), 'passwords.db')

    def __init__(self):
        self._db_connection = sqlite3.connect(self.db_file)
        self._db_cursor = self._db_connection.cursor()

    def query(self, query, params: list = None):
        if params is None:
            params = []
        return self._db_cursor.execute(query, params)

    def __del__(self):
        self._db_connection.commit()
        self._db_connection.close()


if __name__ == '__main__':
    sql = """
        CREATE TABLE IF NOT EXISTS passwords (
        id integer PRIMARY KEY,
        name text NOT NULL UNIQUE,
        password text NOT NULL
        );
    """
    db_object = DBConnection()
    db_object.query(sql)
