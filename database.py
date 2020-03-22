import os
import sqlite3
from sqlite3 import Cursor

import pyperclip

from password import Password


class DBConnection:
    db_file = os.path.join(os.environ.get('SQLITE_DB_PATH', os.path.abspath(os.getcwd())), 'passwords.db')

    def __init__(self):
        self._db_connection = sqlite3.connect(self.db_file)
        self._db_cursor = self._db_connection.cursor()

    def query(self, query: str, params: list = None) -> Cursor:
        if params is None:
            params = []
        return self._db_cursor.execute(query, params)

    def __del__(self):
        self._db_connection.commit()
        self._db_connection.close()

    @classmethod
    def create_password_and_save(cls, name: str) -> None:
        sql = """
        INSERT INTO passwords (name, password)
        VALUES (?, ?)
        """

        password = Password()
        db_object = DBConnection()
        db_object.query(sql, [name, str(password)])
        pyperclip.copy(str(password))
        print(f"You added password for {name}. Password has been copied to clipboard.")

    @classmethod
    def create_table(cls) -> None:
        sql = """
            CREATE TABLE IF NOT EXISTS passwords (
            id integer PRIMARY KEY,
            name text NOT NULL UNIQUE,
            password text NOT NULL
            );
        """
        db_object = DBConnection()
        db_object.query(sql)

    @classmethod
    def get_password_from_db(cls, name: str) -> None:
        sql = "SELECT name, password FROM passwords WHERE name LIKE ?"
        db_object = DBConnection()
        result = db_object.query(sql, [name])
        if result.rowcount():
            pyperclip.copy(result.fetchone()[1])
            print(f"Your password for {name} was copied to clipboard")
        else:
            print(f"There is no result for {name}. Try to take all names and get the correct one")

    @classmethod
    def get_all_passwords(cls):
        sql = "SELECT name FROM passwords"

        db_object = DBConnection()
        result = db_object.query(sql)

        if result.rowcount:
            print(f"You have saved passwords for:")
            for index, row in enumerate(result.fetchall(), 1):
                print(f"{index}. {row[0]}")
        else:
            print(f"You haven't saved any passwords yet.")


if __name__ == '__main__':
    DBConnection.create_table()
