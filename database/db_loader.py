import sqlite3
from utility.constants import FILE


def db_loader(sql_file_path):
    try:
        connection = sqlite3.connect(FILE.DB_FILE)
        cursor = connection.cursor()
        sql_file = open(sql_file_path)
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)
        return True
    except (OSError, ConnectionError):
        print('Error while loading sql file')
