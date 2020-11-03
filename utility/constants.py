import os


class Mode:
    MIGRATION = "migration"
    EXECUTE = "execute"


class FILE:
    SQL_FILE = "db.sql"
    MIGRATION_FILE = "migration.sql"
    DB_FILE = str(os.getcwd()) + "/data.db"


class PARAM:
    MIGRATION = 'migration'
    PROCESS = 'process'


class SHOP:
    SHOP_ID = 0
    DATE = 1
    BUDGET = 2
    EXPENDITURE = 3


