from tkinter import *


class TransactionView:

    def __init__(self, master):
        self.master = master

        # left side of menu
        self.desc_text = Label(text='Choose a transaction', font=('Arial', 14), background='#88C9ED')
        self.deposit = Button(text='Deposit', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw = Button(text='Withdrawal', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.balance = Button(text='Balance', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

        # right side of menu
        self.trans_hist = Button(text='Transaction\nhistory', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.quick_withdraw = Button(text='Quick\nwithdraw $60', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.logout = Button(text='Logout', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=2)

        # left side of menu
        self.deposit.grid(row=1)
        self.withdraw.grid(row=2)
        self.balance.grid(row=3)

        # right side of menu
        self.trans_hist.grid(row=1, column=1)
        self.quick_withdraw.grid(row=2, column=1)
        self.logout.grid(row=3, column=1)

        # row configuring
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(3, weight=1)

        # column configuring
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.deposit.grid_remove()
        self.withdraw.grid_remove()
        self.balance.grid_remove()
        self.trans_hist.grid_remove()
        self.trans_hist.grid_remove()
        self.quick_withdraw.grid_remove()
        self.logout.grid_remove()

        # row configuring
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(3, weight=0)

        # column configuring
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)


if __name__ == '__main__':
    root = Tk()
    TransactionView(root)
    mainloop()
