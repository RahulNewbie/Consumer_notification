import sqlite3


class Database:
    def __init__(self, db_file_path):
        self.config = db_file_path
        self.connection = None
        self._prepare_connection()

    def __del__(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def __enter__(self):
        return self

    def __exit__(self):
        self.connection.close()
        self.connection = None

    def _prepare_connection(self):
        """ Creates a new connection if it was not
            created yet or was closed
        """

        try:
            if self.connection is None:
                self.connection = sqlite3.connect(
                    self.config,
                    check_same_thread=False
                )
            print("Database connected successfully........")
        except (Exception, OSError, ConnectionError) as error:
            print(error)

    def get_shops_data(self):
        """
        Query all rows in the screenshot table
        :param: None
        :return: All rows of the table
        """
        try:
            cur = self.connection.cursor()
            # Select All the records from the Database
            cur.execute("SELECT * FROM t_budgets")
            rows = cur.fetchall()
            for row in rows:
                yield row
        except(OSError, ConnectionError, Exception) as excep:
            print("Error occurred while fetching data "
                  "from database {}".format(str(excep)))

    def set_shop_offline(self, shop_id):
        try:
            cur = self.connection.cursor()
            cur.execute("UPDATE t_shops "
                        "set processed = ? AND a_online = ? WHERE a_id = ? ", (1, 1, shop_id,))
        except (OSError, ConnectionError, Exception) as excep:
            print("Error occurred while setting shop offline "
                  "{}".format(str(excep)))

    def check_if_processed(self, shop_id):
        try:
            cur = self.connection.cursor()
            cur.execute("SELECT * FROM t_shops "
                        "WHERE a_id = ? and processed = ?",
                        (shop_id, 1,))
            rows = cur.fetchall()
            if len(rows) > 1:
                return True
            else:
                return False
        except (OSError, ConnectionError, Exception) as excep:
            print("Error occurred while checking processed data "
                  "{}".format(str(excep)))

