from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD SEARCH ------------------------------- #

def search():
    website_search_key = website_entry.get()
    if website_search_key == "":
        messagebox.showinfo(title="Password Manager", message="Website field cannot be empty")
    else:
        try:
            with open("data.json", "r") as json_file:
                data_dict = json.load(json_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Password Manager", message="You have no passwords stored.")
        else:
            try:
                password_search_key = data_dict[website_search_key]["password"]
            except KeyError:
                messagebox.showinfo(title="Password Manager", message="You don't have a password stored for the requested website.")
            else:
                messagebox.showinfo(title="Password Manager", message=f"Your password for {website_search_key} is {password_search_key}.\nPassword copied to clipboard!")
                pyperclip.copy(password_search_key)

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
    password_entry.delete(0, END)
    password_entry.insert(0,gen_password)
    messagebox.showinfo(title="Password Manager", message="Generated password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "password": password,
            "email": email
        }
    }
    if website == "" or password == "" or email == "":
        messagebox.showinfo(title="Password Manager", message="Field(s) cannot be empty.")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager",
                                       message=f"These are the details entered:\n\nWebsite: {website}\n\nEmail: {email}\n\nPassword: {password}\n\nDo you want to save?")
        if is_ok:
            try:
                with open("data.json", "r") as json_file:
                    data_dict = json.load(json_file)
            except FileNotFoundError:
                with open("data.json", "w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            except JSONDecodeError:
                with open("data.json", "w") as json_file:
                    json.dump(new_data, json_file, indent=4)
            else:
                data_dict.update(new_data)

                with open("data.json", "w") as json_file:
                    json.dump(data_dict, json_file, indent=4)
            finally:
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
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan = 2, pady=5)
email_entry.insert(0, "shraveen@gmail.com")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, pady=5)

# Button
generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(row=3, column=2, padx=5)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5)
search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
