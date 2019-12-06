from tkinter import *


class LoginView:

    def __init__(self, master):
        self.master = master
        self.master.title("NZS ATM's")
        self.master.geometry('600x400')
        self.master.config(background='#88C9ED')

        # menu creation
        self.desc_text = Label(text='Login', font=('Arial', 14), background='#88C9ED')
        self.qr_label = Label(text='Scan the QR code to login\nOR\nLogin with your credit card', font=('Arial', 14), background='#88C9ED')
        self.card_num_label = Label(text='Enter your card number', font=('Arial', 14), background='#88C9ED')
        self.card_pin_label = Label(text='Enter your pin number', font=('Arial', 14), background='#88C9ED')
        self.card_num_entry = Entry(width=25, font=('Arial', 14))
        self.card_pin_entry = Entry(width=25, font=('Arial', 14))
        self.login_button = Button(text='Login', width=10, height=3, font=('Arial', 14), background='#B2E2EE')
        self.qr_temp = Button(text='QR Code', width=10, height=3, font=('Arial', 14))
        self.error_label = Label(font=('Arial', 14), background='#88C9ED', fg='red')

    def show_menu(self):
        self.desc_text.grid(row=0, columnspan=2)
        self.qr_label.grid(row=1)
        self.qr_temp.grid(row=1, column=1)
        self.card_num_label.grid(row=2, sticky=N)
        self.card_pin_label.grid(row=3, sticky=N)
        self.card_num_entry.grid(row=2)
        self.card_pin_entry.grid(row=3)
        self.login_button.grid(row=2, column=1, rowspan=2)
        self.error_label.grid(row=4)

        # row configuring
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_rowconfigure(4, weight=1)

        # column config
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

    def hide_menu(self):
        self.desc_text.grid_remove()
        self.qr_label.grid_remove()
        self.card_num_label.grid_remove()
        self.card_pin_label.grid_remove()
        self.card_num_entry.grid_remove()
        self.card_pin_entry.grid_remove()
        self.login_button.grid_remove()
        self.qr_temp.grid_remove()
        self.error_label.grid_remove()

        # row configuring
        self.master.grid_rowconfigure(0, weight=0)
        self.master.grid_rowconfigure(1, weight=0)
        self.master.grid_rowconfigure(2, weight=0)
        self.master.grid_rowconfigure(3, weight=0)

        # column config
        self.master.grid_columnconfigure(0, weight=0)
        self.master.grid_columnconfigure(1, weight=0)


if __name__ == '__main__':
    root = Tk()
    LoginView(root)
    mainloop()
