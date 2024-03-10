from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    gen_password = "".join(password_list)

    pyperclip.copy(gen_password)
    password_entry.insert(0,gen_password)
    messagebox.showinfo(title="Password Manager", message="Generated password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title="Password Manager",
                                   message=f"These are the details entered:\n\nWebsite: {website}\n\nEmail: {email}\n\nPassword: {password}\n\nDo you want to save?")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Password Manager", message="Password saved successfully!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website = Label(text="Website: ")
website.grid(row=1, column=0)
email = Label(text="Email/ Username: ")
email.grid(row=2, column=0)
password = Label(text="Password")
password.grid(row=3, column=0)

# Text Area and Entry
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, pady=5)
email_entry.insert(0, "shraveen@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, pady=5)

# Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2, padx=5)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()
