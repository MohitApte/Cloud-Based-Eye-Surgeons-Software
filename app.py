from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter as tk
import ttkthemes
from reportlab.pdfgen import canvas
from ttkthemes import ThemedStyle
import datetime
import pyautogui as pg
import time
from PIL import Image
import subprocess
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from docx import Document
from PIL import Image
from tkinter import Tk, Label, Button, filedialog
from pymongo import MongoClient
from PIL import Image
import io
from docx.shared import Inches
from tkinter import messagebox
import ssl
import certifi
import win32api
import win32print
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
ca = certifi.where()



# Universal resourse identification
uri = "mongodb+srv://mohitapte4:j3ZsXs6FGCnGATZm@cluster0.xmn1i2w.mongodb.net/?retryWrites=true&w=majority"

# Create a client object of class MongoClient
client = MongoClient(uri,tlsCAFile=ca)

# Function for User-Login validation
def validateLogin(username, password):    
    db = client['patient_data']
    collection = db['passwd']
    user = collection.find_one({"username": username.get(), "password": password.get()})
    if user:
        main_page()
    else:
       messagebox.showerror("Error", "Invalid Login Id or Password")


# Required lists for further project
x = []
medname = []
medtype = []
medadvice = []
days = []
dwm = []
qty = []
img_data = ""


def draw_multiline_text(canvas, text, x, y, width, height, font_size):
    lines = []
    current_line = ""
    words = text.split()
    max_line_height = 0

    for word in words:
        if canvas.stringWidth(current_line + " " + word, "Helvetica", font_size) < width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    for line in lines:
        line_height = canvas.stringWidth(line, "Helvetica", font_size)
        if line_height > max_line_height:
            max_line_height = line_height

    total_lines = len(lines)
    remaining_height = height - (total_lines * max_line_height)
    y -= max_line_height

    for line in lines:
        canvas.drawString(x, y, line.strip())
        y -= max_line_height

    return remaining_height



class Patient():
    def __init__(self, mrd,fn,mn,ln,age,sex,address,mob,land,misc):
        self.mrd = mrd
        self.fn = fn
        self.mn = mn
        self.ln = ln
        self.age = age
        self.sex = sex
        self.address = address
        self.mob = mob
        self.land = land
        self.misc = misc
        
def main_page():
    # Toplevel() is a class in Tkinter used to create independent windows (also known as "top-level windows" or "child windows") that are separate from the main application window (Tk() window). 
    app = Toplevel(root)

    # retrieve the width of the screen where the app window is currently located.
    screen_width = app.winfo_screenwidth()
    # retrieve the height in same way
    screen_height = app.winfo_screenheight()
    

    # sets the geometry of the app window to be equal to the width and height of the screen
    app.geometry("%dx%d" % (screen_width, screen_height))
    
    # creates a notebook-style tab control (ttk.Notebook) inside the app window. The tabControl variable is used to reference this tab control.
    tabControl = ttk.Notebook(app)
    
    # creates a frame (ttk.Frame) named tab1 to serve as the content of the first tab. This frame is added as a tab to the tabControl notebook.
    tab1 = ttk.Frame(tabControl)
    # tab 2
    tab2 = ttk.Frame(tabControl)

    # adds tab1 as a tab to the tabControl notebook, with the text label Out Patient Department
    tabControl.add(tab1, text ='Out Patient Department')
    # adds tab2 as a tab to the tabControl notebook, with the text label In Patient Department
    tabControl.add(tab2, text ='In Patient Department')


    # This packs the tabControl notebook inside the app window, causing it to expand to fill the available space in both the horizontal and vertical directions.
    tabControl.pack(expand = 1, fill ="both")
    
    # This creates a button (ttk.Button) inside tab1 with the specified text label "New Patient" and associates it with the "new_patient" function. The button is positioned using the grid geometry manager at row 1, column 0 within tab1.
    ttk.Button(tab1, text="New Patient", command=new_patient).grid(row=1, column=0) 
    # button in row 1 , col 1 -- "old_patient" function
    ttk.Button(tab1, text="Old Patient", command=old_patient).grid(row=1, column=1)


root = Tk()
root.geometry("400x150")
root.title("Ophthalmic Software")


# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")


usernameLabel = ttk.Label(root, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = ttk.Entry(root, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = ttk.Label(root,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = ttk.Entry(root, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)
#login button
loginButton = ttk.Button(root, text="Login", command=validateLogin).grid(row=4, column=0)  


root.mainloop()





