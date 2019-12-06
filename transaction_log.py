from datetime import datetime


class Log:

    def __init__(self):
        self.transactions = []

    def new_log(self, desc: str, amount: str, balance: str):
        time = str(datetime.today())[0:10]
        self.transactions = [time, desc, amount, balance]