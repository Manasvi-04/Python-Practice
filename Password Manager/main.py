from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbol + password_number + password_letter

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FILE SEARCH ------------------------------#
def find_password():
    website = website_input.get()
    try:
        with open("saved_password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for this {website} found")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    password = password_input.get()
    email = email_input.get()
    new_dic = {
        website: {
            "email": email,
            "password": password
        }
    }


    if len(password) == 0 or len(email) == 0 or len(website) == 0:
        messagebox.showinfo(title="Alert!!!", message="Please make sure you haven't left any of the fields empty!!! ")
    else:
        try:
            with open("saved_password.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("saved_password.json", mode="w") as file:
                json.dump(new_dic, file, indent=4)
        else:
            data.update(new_dic)
            with open("saved_password.json", mode="w") as file:
                json.dump(data, file, indent=4)



        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=200)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=18)
website_input.focus()
website_input.grid(column=1, row=1)

search_button = Button(text="Search", width=17, command=find_password)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=40)
email_input.insert(0, "@gmail.com")
email_input.grid(column=1, row=2, columnspan=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=18)
password_input.grid(column=1, row=3, columnspan=1)

password_button = Button(text="Generate Password ", width=17, command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()