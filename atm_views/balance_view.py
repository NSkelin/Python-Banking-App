from tkinter import *


class BalanceView:

    def __init__(self, master):
        self.master = master

        self.desc_text = Label(text='Balance', font=('Arial', 14), background='#88C9ED')
        self.balance_amt = Label(font=('Arial', 14))
        self.accept = Button(text='Ok', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

    def show_balance(self, amount):
        self.balance_amt.config(text='$ ' + str(amount))

    def show_menu(self):
        self.desc_text.grid(row=0)
        self.balance_amt.grid(row=1, sticky=N)
        self.accept.grid(row=2, sticky=N)

        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=4)

        self.master.grid_columnconfigure(0, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.balance_amt.grid_remove()
        self.accept.grid_remove()
