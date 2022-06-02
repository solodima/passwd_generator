from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = username_entry.get()
    passwd = password_entry.get()

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops!", message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n'
                                                              f'website: {website}\n'
                                                              f'password: {passwd}\n'
                                                              'Save?')
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{website} | {username} | {passwd}\n')

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

add_button = Button(width=36, text='Add', command=save)
add_button.grid(row=4, column=1, columnspan=2)
generate_password_button = Button(width=14, text='Generate Password', command=generate)
generate_password_button.grid(row=3, column=2)

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
username_entry = Entry(width=36)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'dmitry.solodukho@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()
