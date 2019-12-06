import csv
import os.path


class BankModel:

    def __init__(self):
        self.my_path = os.path.abspath(os.path.dirname(__file__))
        self.filename = os.path.join(self.my_path, 'account_details.csv')

    def read_file(self, filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            file_list = list(csv_reader)
            return file_list

    def write_file(self, filename, file_data):
        with open(filename, 'w', newline='') as new_file:
            csv_file = csv.writer(new_file)
            csv_file.writerows(file_data)

    def verify_account(self, number, pin):
        users_file = self.read_file(self.filename)
        for line in users_file:
            if line[0] == number:
                if line[1] == pin:
                    return True
        return False

    def get_acc_details(self, card_num: str):
        users_file = self.read_file(self.filename)
        for line in users_file:
            if line[0] == card_num:
                return line

    def change_balance(self, card_num: str, amount: float):
        users_file = self.read_file(self.filename)
        for line in users_file:
            if line[0] == card_num:
                balance = float(line[4])
                balance += round(amount, 2)
                line[4] = str(balance)
        self.write_file(self.filename, users_file)

    def add_log(self, filename, log):
        if os.path.isfile(filename):
            users_logs = self.read_file(filename)
            users_logs.append(log)
            self.write_file(filename, users_logs)
        else:
            new_log = [['time', 'action', 'amount', 'balance'], log]
            self.write_file(filename, new_log)

    def next_card_num(self):
        file = self.read_file('next_card_num.csv')
        new_num = int(file[1][0])
        new_num += 1
        file[1][0] = str(new_num)
        self.write_file('next_card_num.csv', file)
        return new_num

    def add_account(self, pin, fname, lname):
        file = self.read_file(self.filename)
        card_num = self.next_card_num()
        file.append([card_num, pin, fname, lname, 0.0])
        self.write_file(self.filename, file)
        return card_num


if __name__ == '__main__':
    test = BankModel()
    print(test.read_file('account_details.csv'))
    test.change_balance('1111', 1000)
    print(test.get_acc_details('1111'))
    print(test.my_path)
    print(test.filename)
