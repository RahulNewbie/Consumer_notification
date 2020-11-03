import sys
import time

from utility.constants import FILE
from database.db_loader import db_loader
from service.service import Retailers

if __name__ == '__main__':
    if sys.argv[1] == "migration":
        try:
            db_loader(FILE.SQL_FILE)
            db_loader(FILE.MIGRATION_FILE)
            print('Database load and migration successful')
        except (OSError, ConnectionError):
            print('Database load unsuccessful')
    elif sys.argv[1] == "process":
        # Create retailer object to start the thread
        retailer_thread = Retailers(FILE.DB_FILE)
        while True:
            time.sleep(60)  # Wait for 60 seconds
