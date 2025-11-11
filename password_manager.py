from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import pickle
import re

# ---------------------------- MODEL SETUP ------------------------------- #

model = pickle.load(open("strength_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
strength_map = {0: "Weak", 1: "Medium", 2: "Strong"}

def predict_strength(password):
    vect = vectorizer.transform([password])
    pred = model.predict(vect)[0]
    if isinstance(pred, (int, float)):
        return strength_map.get(int(pred), "Unknown")
    else:
        return str(pred).capitalize()

def evaluate_strength(password):
    if not password or len(password) < 4:
        return "Weak"
    if password.isdigit():
        return "Weak"

    score = 0
    if len(password) >= 8: score += 1
    if re.search("[a-z]", password): score += 1
    if re.search("[A-Z]", password): score += 1
    if re.search("[0-9]", password): score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password): score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
strength_label = Label(text="Strength: —", font=("Arial", 10, "bold"))
strength_label.grid(row=5, column=1)

def color_strength(strength):
    colors = {"Weak": "red", "Medium": "orange", "Strong": "green"}
    strength_label.config(fg=colors.get(strength, "black"), text=f"Strength: {strength}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    strength = evaluate_strength(password)
    color_strength(strength)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
    )
    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        strength_label.config(text="Strength: —", fg="black")

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
        return
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- ENTRY & BUTTONS ------------------------------- #

website_entry = Entry(width=17)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=34)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "samaygangwal21@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)
password_entry.bind("<KeyRelease>", lambda e: color_strength(evaluate_strength(password_entry.get())))

generate_password_button = Button(text="Generate Password", command=generate_password, width=13)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)

window.mainloop()
