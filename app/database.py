import sqlite3

DATABASE_NAME = 'database/database.db'

def db_connect(func):
    def wrapper(*args, **kwargs):
        connect = sqlite3.connect(DATABASE_NAME)
        cursor = connect.cursor()
        args += (cursor,)
        result = func(*args, **kwargs)
        connect.commit()
        connect.close()
        return result
    return wrapper

@db_connect
def test_create(cursor):
    cursor.execute("DROP TABLE IF EXISTS Users;")
    cursor.execute('CREATE TABLE Users (username TEXT NOT NULL,password TEXT NOT NULL);')
    cursor.execute('INSERT INTO Users VALUES (\'admin\', \'hard\')')
    cursor.execute('INSERT INTO Users VALUES (\'jayse\', \'1337\')')

@db_connect
def test_select(username, cursor):
    cursor.execute("SELECT * FROM Users WHERE username = \"{}\";".format(username))
    return cursor.fetchall()

@db_connect
def test_select_all(cursor):
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()