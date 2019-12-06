from tkinter import *


class Prompt:

    def __init__(self, master):
        self.master = master

        self.desc_text = Label(text='Would you like to make another transaction?', font=('Arial', 14), background='#88C9ED')
        self.accept = Button(text='Yes', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.decline = Button(text='No', width=10, height=3, font=('Arial', 14), background='#B2E2EE')

    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=2)
        self.accept.grid(row=1, column=0)
        self.decline.grid(row=1, column=1)

        # row configuring
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=4)

        # column configuring
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.accept.grid_remove()
        self.decline.grid_remove()

        # row configuring
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)

        # column configuring
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)
