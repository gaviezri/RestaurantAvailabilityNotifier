import json
from constants import Constants
from driver.DOMDriver import DOMDriver
from notifier.Notifier import Notifier
from datetime import datetime


def delay_1_hour():
    now = datetime.now()
    while abs(now.hour == datetime.now().hour):
        pass


class MainDriver:
    @staticmethod
    def run():
        config = json.load(open("./config.json"))
        url = config["rest_url"]

        notifier = Notifier(credentials={"username": input("username:"), "password": input("password:")},
                            receipients=config["targets"],
                            url=url,
                            is_test=True)

        dom_driver = DOMDriver(url)
        while datetime.now() < Constants.end_date:
            is_available, when = dom_driver.check_availability()
            if is_available:
                notifier.notify(when)
            delay_1_hour()
