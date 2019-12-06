from transaction_log import Log


class Account:

    def __init__(self, card_num, fname: str, lname: str, balance=0):
        self.acc_num = card_num
        self.fname = fname
        self.lname = lname
        self.user_file = '{}_{}_log.csv'.format(self.fname, self.lname)
        try:
            self._balance = float(balance)
        except TypeError:
            print('Error: Balance must be number')
        self.log = Log()

    def withdraw(self, amt: float):
        try:
            if self._balance >= amt:
                if amt <= 0:
                    print("Error: Cannot be a negative number")
                else:
                    amt = round(amt, 2)
                    self._balance -= amt
                    self.log.new_log('Withdrawal', str(amt), str(self.balance))
                    return True
            else:
                print("Withdrawal failed, insufficient funds")
        except TypeError:
            print("Withdrawal error: Must input an integer")

    def deposit(self, amt: float):
        try:
            if amt <= 0:
                print("Error: Cannot be a negative number")
            else:
                amt = round(amt, 2)
                self._balance += amt
                self.log.new_log('Deposit', str(amt), str(self.balance))
                return True
        except TypeError:
            print('Deposit Error: Must input an integer')

    @property
    def balance(self):
        return self._balance

    def change_name(self, name: str):
        if isinstance(name, str):
            self.name = name
        else:
            print("New name must be letters")

    def fee(self):
        amt = 25
        if self._balance >= amt:
            self._balance -= amt
            self.log.new_log('Fee charged', amt)
            return
        else:
            print('Failed to charge fee')
            return

    def pay_interest(self):
        rate = 0.04
        amt = self._balance * rate
        self._balance += self._balance * rate
        self.log.new_log('Interest deposited', amt)

    def __str__(self):
        return 'Name: {} \nAccount number: {} \nBalance: {}'.format(self.name, self.acc_num, self._balance)


if __name__ == '__main__':
    # testing account functions
    acc1 = Account(1111, 'Bill', 'Bobby')
    print(acc1)
    acc1.deposit(100)
    acc1.deposit(100.35)
    acc1.withdraw(50)
    acc1.withdraw(50.1)
    print(acc1.log.show_transactions())
    print()
    acc1.change_name('Nick, Skelin')
    print(acc1)

    # Testing account error handling
    acc1.deposit('20')
    acc1.deposit(-25)
    acc1.deposit(['20', 30])
    acc1.withdraw('2000')
    acc1.withdraw(-20)
    acc1.change_name(100)
    print(acc1)
