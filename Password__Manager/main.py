import json
import os
import base64
import hashlib
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from cryptography.fernet import Fernet
import pyperclip

# Constants
MASTER_HASH_FILE = "master.hash"
DATA_FILE = "data.json"
KEY_FILE = "key.key"

# ---------------------------- SECURITY SETUP ------------------------------- #
def get_fernet():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = get_fernet()

def hash_master_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate():
    if not os.path.exists(MASTER_HASH_FILE):
        def set_password():
            pwd = entry.get()
            if len(pwd) < 4:
                messagebox.showerror("Weak", "Use a longer password")
                return
            with open(MASTER_HASH_FILE, "w") as f:
                f.write(hash_master_password(pwd))
            auth_window.destroy()

        auth_window = Tk()
        auth_window.title("Set Master Password")
        Label(auth_window, text="Set Master Password:").pack()
        entry = Entry(auth_window, show="*")
        entry.pack()
        Button(auth_window, text="Set", command=set_password).pack()
        auth_window.mainloop()
    else:
        def verify_password():
            pwd = entry.get()
            with open(MASTER_HASH_FILE, "r") as f:
                saved_hash = f.read()
            if saved_hash == hash_master_password(pwd):
                auth_window.destroy()
            else:
                messagebox.showerror("Incorrect", "Wrong master password")

        auth_window = Tk()
        auth_window.title("Enter Master Password")
        Label(auth_window, text="Enter Master Password:").pack()
        entry = Entry(auth_window, show="*")
        entry.pack()
        Button(auth_window, text="Login", command=verify_password).pack()
        auth_window.mainloop()

# ---------------------------- DATA LOAD/SAVE ------------------------------- #
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as f:
        encrypted = f.read()
    decrypted = fernet.decrypt(encrypted)
    return json.loads(decrypted)

def save_data(data):
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(DATA_FILE, "wb") as f:
        f.write(encrypted)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'
    password_list = [choice(letters) for _ in range(randint(8, 10))] + \
                    [choice(symbols) for _ in range(randint(2, 4))] + \
                    [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showerror("Oops", "Website and password cannot be empty.")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        data = load_data()
    except Exception as e:
        data = {}

    data.update(new_data)
    save_data(data)
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        data = load_data()
    except:
        messagebox.showerror("Error", "No data file found or file is corrupted.")
        return

    if website in data:
        messagebox.showinfo(website, f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
    else:
        messagebox.showerror("Not Found", f"No details for {website}")

# ---------------------------- EDIT PASSWORD ------------------------------- #
def edit_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    try:
        data = load_data()
    except:
        messagebox.showerror("Error", "Cannot read data.")
        return

    if website in data:
        data[website] = {
            "email": email,
            "password": password
        }
        save_data(data)
        messagebox.showinfo("Success", "Password updated.")
    else:
        messagebox.showerror("Error", f"{website} not found")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
authenticate()

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your_email@example.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
Button(text="Add", width=36, command=add_password).grid(row=4, column=1, columnspan=2)
Button(text="Edit", width=36, command=edit_password).grid(row=5, column=1, columnspan=2)
Button(text="Search", width=13, command=find_password).grid(row=1, column=2)

window.mainloop()
