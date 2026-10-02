
from tkinter import *
import bcrypt

def validate(password):
    hash = b'$2b$12$Hgcv1KuO9oddItT1lIBmdO.QwKsw7yRy4B0qLMAy/YLslO4b4PJ4i'
    password = bytes(password, encoding='utf-8')

    if bcrypt.checkpw(password,hash):
        print("Login Successfully")
    else:
        print("Invalid Password")




root = Tk()
root.geometry("350x350")

password_entry = Entry(root)
password_entry.pack()


button = Button(root,text="Validate",command = lambda: validate(password_entry.get()))
button.pack()













root.mainloop()




