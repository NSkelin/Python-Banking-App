from tkinter import *


class DepositView:

    def __init__(self, master):
        self.master = master

        self.desc_text = Label(text='Deposit', font=('Arial', 14), background='#88C9ED')
        self.amt_entry = Entry(width=25, font=('Arial', 14))
        self.amt_entry_label = Label(text='$', font=('Arial', 14), background='#88C9ED')
        self.accept = Button(text='Accept', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.cancel = Button(text='Cancel', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.error_label = Label(font=('Arial', 14), background='#88C9ED', fg='red')

        # place onto grid
    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=2)
        self.amt_entry.grid(row=1, columnspan=2)
        self.amt_entry_label.grid(row=1)
        self.accept.grid(row=2, sticky=N)
        self.cancel.grid(row=2, column=1, sticky=N)
        self.error_label.grid(row=3,columnspan=2)

        # row configure
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=3)
        self.master.grid_rowconfigure(3, weight=10)

        # column configure
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.amt_entry.grid_remove()
        self.amt_entry_label.grid_remove()
        self.accept.grid_remove()
        self.cancel.grid_remove()
        self.error_label.grid_remove()

        # row configure
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_rowconfigure(3, weight=0)

        # column configure
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
