import sys

import pyperclip

from database import DBConnection

if __name__ == '__main__':

    try:
        name = sys.argv[1]
    except IndexError:
        print("Enter the name for password:")
        name = input()

    sql = "SELECT name, password FROM passwords WHERE name LIKE ?"
    db_object = DBConnection()
    result = db_object.query(sql, [name])
    if result.rowcount():
        pyperclip.copy(result.fetchone()[1])
        print(f"Your password for {name} was copied to clipboard")
    else:
        print(f"There is no result for {name}. Try to take all names and get the correct one")
