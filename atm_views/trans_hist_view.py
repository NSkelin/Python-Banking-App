from tkinter import *


class HistoryView:

    def __init__(self, master):
        self.master = master

        self.desc_text = Label(text='Transaction history', font=('Arial', 14), background='#88C9ED')
        self.accept = Button(text='Ok', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

        self.text = StringVar(self.master)
        self.text.set('Newest')
        self.filter = OptionMenu(self.master, self.text, 'Newest', 'Oldest')
        self.filter.config(font=('Arial', 14), background='#B2E2EE')

        self.log_display = Listbox(width=50, height=10, font=('Arial', 11), borderwidth=0)

        self.filter_but = Button(text='Filter', font=('Arial', 14), background='#B2E2EE')

    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=4)
        self.accept.grid(row=1, column=2)
        self.filter.grid(row=1, column=0, sticky=SE)
        self.log_display.grid(row=2, columnspan=4)
        self.filter_but.grid(row=1, column=1, sticky=SW)

        # row configuring
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)

        # column configuring
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.accept.grid_remove()
        self.filter.grid_remove()
        self.log_display.grid_remove()
        self.filter_but.grid_remove()

        # row configuring
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=0)

        # column configuring
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
        self.master.grid_columnconfigure(2, weight=0)
