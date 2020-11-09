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

    cursor.execute("DROP TABLE IF EXISTS Messages;")
    cursor.execute('CREATE TABLE Messages (username TEXT NOT NULL, messaage TEXT NOT NULL);')
    cursor.execute('INSERT INTO Messages VALUES (\'user\', \'text\')')


@db_connect
def add_user(cursor, username, password):
    cursor.execute(f'INSERT INTO Users VALUES (\'{username}\', \'{password}\')')


@db_connect
def user_exists(cursor, username, password):
    cursor.execute(f'SELECT \'{username}\' FROM Users;')
    if not cursor.fetchall():
        return True
    else:
        return False


@db_connect
def user_entered_the_pass(cursor, username, password):
    cursor.execute(f'SELECT \'{username}\' FROM Users;')
    if password == cursor.fetchall()[1]:
        return True
    else:
        return False


@db_connect
def add_message(cursor, username, message):
    cursor.execute(f'INSERT INTO Messages VALUES (\'{username}\', \'{message}\')')


@db_connect
def test_select(username, cursor):
    cursor.execute("SELECT * FROM Users WHERE username = \"{}\";".format(username))
    return cursor.fetchall()


@db_connect
def select(username, cursor):
    cursor.execute("SELECT * FROM Users WHERE username = \"{}\";".format(username))
    return cursor.fetchall()


@db_connect
def test_select_all(cursor):
    cursor.execute("SELECT * FROM Users;")
    return cursor.fetchall()


@db_connect
def select_all_messages(cursor):
    cursor.execute("SELECT * FROM Messages;")
    return cursor.fetchall()
