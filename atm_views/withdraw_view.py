from tkinter import *


class WithdrawView:

    def __init__(self, master):
        self.master = master

        self.desc_text = Label(text='Withdrawal', font=('Arial', 14), background='#88C9ED')
        self.withdraw_20 = Button(text='Withdraw 20', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw_40 = Button(text='Withdraw 40', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw_60 = Button(text='Withdraw 60', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw_80 = Button(text='Withdraw 80', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw_100 = Button(text='Withdraw 100', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.withdraw_cancel = Button(text='Cancel', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=2)
        self.withdraw_20.grid(row=1)
        self.withdraw_40.grid(row=2)
        self.withdraw_60.grid(row=3)
        self.withdraw_80.grid(row=1, column=1)
        self.withdraw_100.grid(row=2, column=1)
        self.withdraw_cancel.grid(row=3, column=1)

        # row configure
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(3, weight=1)

        # column configure
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.withdraw_20.grid_remove()
        self.withdraw_40.grid_remove()
        self.withdraw_60.grid_remove()
        self.withdraw_80.grid_remove()
        self.withdraw_100.grid_remove()
        self.withdraw_cancel.grid_remove()

        # row configure
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(3, weight=0)

        # column configure
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
