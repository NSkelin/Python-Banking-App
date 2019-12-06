from tkinter import *
from account import Account
from bank_model import BankModel
# imports views
from atm_views.login_view import LoginView
from atm_views.transaction_view import TransactionView
from atm_views.deposit_view import DepositView
from atm_views.withdraw_view import WithdrawView
from atm_views.balance_view import BalanceView
from atm_views.trans_hist_view import HistoryView
from atm_views.prompt_view import Prompt


class AtmController:

    def __init__(self, master):
        self.master = master
        self.bank_model = BankModel()

        # loads the views used in the ATM
        self.login_view = LoginView(self.master)
        self.transaction_view = TransactionView(self.master)
        self.deposit_view = DepositView(self.master)
        self.withdraw_view = WithdrawView(self.master)
        self.balance_view = BalanceView(self.master)
        self.trans_hist_view = HistoryView(self.master)
        self.prompt_view = Prompt(self.master)

        # configs view button controls
        # login page buttons
        self.login_view.login_button.config(command=self.login_but_press)

        # transaction page buttons
        self.transaction_view.deposit.config(command=self.deposit_but_press)
        self.transaction_view.withdraw.config(command=self.withdraw_but_press)
        self.transaction_view.balance.config(command=self.balance_but_press)
        self.transaction_view.trans_hist.config(command=self.transact_log_but_press)
        self.transaction_view.quick_withdraw.config(command=self.withdraw_60)
        self.transaction_view.logout.config(command=self.logout_but_press)

        # deposit page buttons
        self.deposit_view.accept.config(command=self.deposit_accept)
        self.deposit_view.cancel.config(command=self.cancel_but)

        # withdraw page buttons
        self.withdraw_view.withdraw_20.config(command=self.withdraw_20)
        self.withdraw_view.withdraw_40.config(command=self.withdraw_40)
        self.withdraw_view.withdraw_60.config(command=self.withdraw_60)
        self.withdraw_view.withdraw_80.config(command=self.withdraw_80)
        self.withdraw_view.withdraw_100.config(command=self.withdraw_100)
        self.withdraw_view.withdraw_cancel.config(command=self.cancel_but)

        # balance page buttons
        self.balance_view.accept.config(command=self.cancel_but)

        # transaction page history buttons
        self.trans_hist_view.accept.config(command=self.cancel_but)
        self.trans_hist_view.filter_but.config(command=self.filter_but)

        # prompt page buttons
        self.prompt_view.accept.config(command=self.prompt_accept)
        self.prompt_view.decline.config(command=self.prompt_decline)

        # shows the login menu at program start
        self.login_view.show_menu()

    # hides all views in the window
    def hide_all_views(self):
        self.login_view.hide_menu()
        self.transaction_view.hide_menu()
        self.deposit_view.hide_menu()
        self.withdraw_view.hide_menu()
        self.balance_view.hide_menu()
        self.trans_hist_view.hide_menu()
        self.prompt_view.hide_menu()

    # login view page button
    def login_but_press(self):
        card_num = self.login_view.card_num_entry.get()
        card_pin = self.login_view.card_pin_entry.get()
        if self.bank_model.verify_account(card_num, card_pin):
            self.hide_all_views()
            self.transaction_view.show_menu()
            details = self.bank_model.get_acc_details(card_num)
            self.account = Account(details[0], details[2], details[3], details[4])
            self.login_view.card_num_entry.delete(0, END)
            self.login_view.card_pin_entry.delete(0, END)
        else:
            self.login_view.error_label.config(text='Card number or pin incorrect')

    # transaction view page buttons
    def deposit_but_press(self):
        self.hide_all_views()
        self.deposit_view.show_menu()

    def withdraw_but_press(self):
        self.hide_all_views()
        self.withdraw_view.show_menu()

    def balance_but_press(self):
        self.hide_all_views()
        self.balance_view.show_balance(round(self.account.balance, 2))
        self.balance_view.show_menu()

    def transact_log_but_press(self):
        self.hide_all_views()
        file = self.account.user_file
        self.refresh_listbox(self.bank_model.read_file(file))
        self.trans_hist_view.show_menu()

    def quick_withdraw_but_press(self):
        self.withdraw_num(60)

    def logout_but_press(self):
        self.hide_all_views()
        self.account = ''
        self.login_view.show_menu()

    # deposit view page buttons
    def deposit_accept(self):
        try:
            amount = float(self.deposit_view.amt_entry.get())
            if self.account.deposit(amount):
                self.bank_model.change_balance(self.account.acc_num, amount)
                self.bank_model.add_log(self.account.user_file, self.account.log.transactions)

            # changes the views
            self.hide_all_views()
            self.deposit_view.amt_entry.delete(0, END)
            self.prompt_view.show_menu()
        except ValueError:
            self.deposit_view.error_label.config(text='You must enter a number')

    def cancel_but(self):
        self.hide_all_views()
        self.prompt_view.show_menu()

    # withdraw view page buttons
    def withdraw_num(self, amount: float):
        try:
            amount = float(amount)
            if self.account.withdraw(amount):
                amount = -amount
                self.bank_model.change_balance(self.account.acc_num, amount)
                self.bank_model.add_log(self.account.user_file, self.account.log.transactions)

            self.hide_all_views()
            self.prompt_view.show_menu()
        except ValueError:
            print('Error: must enter a number')

    def withdraw_20(self):
        self.withdraw_num(20)

    def withdraw_40(self):
        self.withdraw_num(40)

    def withdraw_60(self):
        self.withdraw_num(60)

    def withdraw_80(self):
        self.withdraw_num(80)

    def withdraw_100(self):
        self.withdraw_num(100)

    # transaction history page buttons
    def refresh_listbox(self, logs, filter_type='Newest'):
        self.trans_hist_view.log_display.delete(0, END)
        if filter_type == 'Newest':
            for log in logs:
                self.trans_hist_view.log_display.insert(1, log)
        if filter_type == 'Oldest':
            for log in logs:
                self.trans_hist_view.log_display.insert(END, log)

    def filter_but(self):
        value = self.trans_hist_view.text.get()
        file = self.bank_model.read_file(self.account.user_file)
        self.refresh_listbox(file, value)

    # prompt view page buttons
    def prompt_accept(self):
        self.hide_all_views()
        self.transaction_view.show_menu()

    def prompt_decline(self):
        self.hide_all_views()
        self.account = ''
        self.login_view.show_menu()


if __name__ == '__main__':
    root = Tk()
    run = AtmController(root)
    mainloop()
