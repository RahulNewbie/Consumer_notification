import threading
import time
from time import strftime
from datetime import date
from utility.constants import SHOP

from database.database import Database


class Retailers(object):
    """
    Class to check Retailers
    """
    def __init__(self, db_file_path, interval=10):
        self.interval = interval
        self.database = Database(db_file_path)
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    @staticmethod
    def _get_current_month():
        return strftime('%m')

    @staticmethod
    def _get_month_from_database(date):
        return date.split("-")[1]

    @staticmethod
    def _check_half_budget_consumption(budget, consumption):
        if consumption > budget/2:
            return True
        else:
            return False

    @staticmethod
    def _check_full_budget_consumption(budget, consumption):
        if consumption >= budget:
            return True
        else:
            return False

    @staticmethod
    def _notify(notification_msg, current_date, shop_id, budget, expenditure):
        print('Notification is sent on {} for {} for the shop id {} '
              'with budget {} and expenditure {} '
              'and consumption percentage {}'.
              format(current_date, notification_msg, shop_id, budget, expenditure, str((expenditure/budget)*100)))

    def run(self):
        """
        Run the application
        It will check, if the
        """
        while True:
            try:
                current_month = self._get_current_month()
                for item in self.database.get_shops_data():
                    if int(current_month) == int(self._get_month_from_database(item[1])):
                        if self._check_full_budget_consumption(
                                int(item[SHOP.BUDGET]),
                                int(item[SHOP.EXPENDITURE])
                        ):
                            if not self.database.check_if_processed(item[0]):
                                self._notify(
                                    "Full consumption of allotted budget",
                                    date.today(),
                                    item[SHOP.SHOP_ID],
                                    int(item[SHOP.BUDGET]),
                                    int(item[SHOP.EXPENDITURE])
                                )
                                self.database.set_shop_offline(item[0])

                        elif self._check_half_budget_consumption(
                                int(item[2]),
                                int(item[3])
                        ):
                            self._notify(
                                "Half Consumption of allotted budget",
                                date.today(),
                                item[SHOP.SHOP_ID],
                                int(item[SHOP.BUDGET]),
                                int(item[SHOP.EXPENDITURE])
                            )

                time.sleep(self.interval)
            except (OSError, ConnectionError, Exception) as exception:
                print(exception)


