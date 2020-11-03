import sys
import time

from utility.constants import FILE
from utility.constants import PARAM

from database.db_loader import db_loader
from service.service import Retailers

if __name__ == '__main__':
    if sys.argv[1] == PARAM.MIGRATION:
        try:
            db_loader(FILE.SQL_FILE)
            db_loader(FILE.MIGRATION_FILE)
            print('Database load and migration successful')
        except (OSError, ConnectionError):
            print('Database load unsuccessful')
    elif sys.argv[1] == PARAM.PROCESS:
        # Create retailer object to start the thread
        retailer_thread = Retailers(FILE.DB_FILE)
        while True:
            time.sleep(600)  # Wait for 10 minutes
    else:
        print("Please use the correct argument to run the application")
