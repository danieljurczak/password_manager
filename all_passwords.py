from database import DBConnection

if __name__ == '__main__':
    sql = "SELECT name FROM passwords"

    db_object = DBConnection()
    result = db_object.query(sql)

    if result.rowcount:
        print(f"You have saved passwords for:")
        for index, row in enumerate(result.fetchall(), 1):
            print(f"{index}. {row[0]}")
    else:
        print(f"You haven't saved any passwords yet.")
