import sys

import pyperclip

from database import DBConnection
from password import Password

if __name__ == '__main__':
    try:
        name = sys.argv[1]
    except IndexError:
        print("Enter the name for password:")
        name = input()

    sql = """
    INSERT INTO passwords (name, password)
    VALUES (?, ?)
    """

    password = Password()
    db_object = DBConnection()
    db_object.query(sql, [name, str(password)])
    pyperclip.copy(str(password))
    print(f"You added password for {name}. Password has been copied to clipboard.")
