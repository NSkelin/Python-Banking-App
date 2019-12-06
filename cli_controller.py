from bank_model import BankModel
from account import Account
import sys


class CliController:

    def __init__(self):
        self.bank_model = BankModel()
        self.pin = ''
        self.num = ''

    def main(self):
        print('Welcome...')
        while True:
            num = self.choose_account()
            if num == 1:
                self.create_account()
            if num == 2:
                if self.edit_account():
                    while True:
                        num = self.account_options()
                        if num == 1:
                            self.print_space()
                            self.print_acc_details()
                        elif num == 2:
                            self.edit_account_details()
                        elif num == 3:
                            self.deposit()
                        elif num == 4:
                            self.withdraw()
                        elif num == 5:
                            self.balance()
                        elif num == 6:
                            self.transaction_history()
                        elif num == 7:
                            self.delete_account()
                        elif num == 8:
                            break
            if num == 3:
                sys.exit()

    def print_space(self):
        print('\n' + ('-' * 50))

    def print_acc_details(self):
        print('Account number: ', self.account.acc_num)
        print('Account type: savings')
        print('Account holder: ', self.account.fname + ' ' + self.account.lname)

    def choose_account(self):
        self.print_space()
        print('Would you like to create or edit an account?')
        print('1 - Create account\n2 - Edit account\n3 - Quit')
        while True:
            num = input('Please enter a number (1-2): ')
            try:
                num = int(num)
                if 0 < num < 4:
                    return num
                else:
                    print('"{}" Is not a valid option'.format(num))
            except ValueError:
                print('"{}" is not a number'.format(num))

    def create_account(self):
        while True:
            self.print_space()
            try:
                print('Creating account...')
                pin = (input('Enter the pin: '))
                if 3 < len(pin) < 5:
                    first_name = str(input('Enter the first name: '))
                    last_name = str(input('Enter the last name: '))
                    int(pin)
                    if first_name.isalpha() and last_name.isalpha():
                        while True:
                            self.print_space()
                            print('Name:', first_name, last_name, '\nPin:', pin)
                            num = int(input('Create this account?\n1 - Yes\n2 - No\n'))
                            if num == 1:
                                card_num = self.bank_model.add_account(pin, first_name, last_name)
                                print('Created account, card num is:\n{}'.format(card_num))
                                return
                            if num == 2:
                                print('Canceled')
                                return
                    else:
                        print('Name must be only characters')
                else:
                    print('Pin must be 4 numbers long')
            except ValueError:
                print('Error: invalid input\nAborting...')

    def edit_account(self):
        self.print_space()
        card_num = input('Please enter the account number: ')
        pin_num = input('Please enter the account pin: ')
        if self.bank_model.verify_account(card_num, pin_num):
            details = self.bank_model.get_acc_details(card_num)
            self.account = Account(details[0], details[2], details[3], details[4])
            self.num = details[0]
            self.pin = details[1]
            return True
        else:
            print('Incorrect')
            return False

    def account_options(self):
        self.print_space()
        self.print_acc_details()
        print('\nChoose an option')
        print('1 - Account info\n2 - Edit account details\n3 - Deposit\n4 - Withdraw\n5 - Balance\n'
              '6 - Transaction history\n7 - Delete Account\n8 - Back')
        while True:
            num = input('Please enter a number (1-8): ')
            try:
                num = int(num)
                if 0 < num < 9:
                    return num
                else:
                    print('"{}" Is not a valid option'.format(num))
            except ValueError:
                print('"{}" is not a number'.format(num))

    def deposit(self):
        while True:
            try:
                amount = float(input('Enter deposit amount: '))
                if self.account.deposit(amount):
                    self.bank_model.change_balance(self.account.acc_num, amount)
                    self.bank_model.add_log(self.account.user_file, self.account.log.transactions)
                    return
                else:
                    print('Failed to deposit')
                    return
            except ValueError:
                print('Type a number')

    def withdraw(self):
        try:
            amount = float(input('Enter withdraw amount: '))
            if self.account.withdraw(amount):
                self.bank_model.change_balance(self.account.acc_num, amount)
                self.bank_model.add_log(self.account.user_file, self.account.log.transactions)
                return
            else:
                print('Failed to withdraw')
                return
        except ValueError:
            print('Error: must enter a number')

    def balance(self):
        self.print_space()
        print('Your balance is: {}'.format(self.account.balance))

    def transaction_history(self):
        self.print_space()
        print('Transaction history for:')
        self.print_acc_details()
        print('1 - Last ten transactions\n2 - All logs')
        num = input('Please enter a number (1-2)')
        file = self.bank_model.read_file(self.account.user_file)
        if num == '1':
            for i in range(11):
                print(file[i])
        elif num == '2':
            for item in file:
                print(item)
            return
        else:
            print('Not an option, Returning...')
            return

    def delete_account(self):
        self.print_space()
        print('Delete account')
        num = input('Re-enter the card number: ')
        pin = input('Re-enter the pin number: ')
        if self.num == num and self.pin == pin:
            self.print_acc_details()
            print('Are you sure you wish to delete this account?\n1 - Yes\n2 - No')
            confirm = input('Please enter a number (1-2): ')
            if confirm == '1':
                file = self.bank_model.read_file(self.bank_model.filename)
                i = 0
                for item in file:
                    if item[0] == self.num:
                        file.pop(i)
                        self.bank_model.write_file(self.bank_model.filename, file)
                        print('Account deleted')
                        return
                    i += 1
            elif confirm == '2':
                print('Canceling...')
                return
            else:
                print('Invalid option, Canceling...')
                return
        else:
            print('Incorrect, Canceling...')

    def edit_account_details(self):
        self.print_space()
        print('What do you want to edit?\n1 - Name\n2 - Pin')
        num = input('Please enter a number (1-2): ')
        if num == '1':
            new_fname = input('Enter a new first name: ')
            self.account.fname = new_fname
            new_lname = input('Enter a new last name: ')
            self.account.lname = new_lname
            file = self.bank_model.read_file(self.bank_model.filename)
            for item in file:
                if item[0] == self.num:
                    item[2] = new_fname
                    item[3] = new_lname
                    self.bank_model.write_file(self.bank_model.filename, file)
                    print('Name changed, new name:\n{} {}'.format(new_fname, new_lname))
            return
        if num == '2':
            new_pin = input('Enter a new pin: ')
            file = self.bank_model.read_file(self.bank_model.filename)
            for item in file:
                if item[0] == self.num:
                    item[1] = new_pin
                    self.num =new_pin
                    self.bank_model.write_file(self.bank_model.filename, file)
                    print('Pin changed, new pin:\n{}'.format(new_pin))
            return
        else:
            print('Invalid option, Canceling...')


if __name__ == '__main__':
    cli = CliController()
    cli.main()
