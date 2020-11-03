import os


class Mode:
    MIGRATION = "migration"
    EXECUTE = "execute"


class FILE:
    SQL_FILE = "db.sql"
    MIGRATION_FILE = "migration.sql"
    DB_FILE = str(os.getcwd()) + "/data.db"


