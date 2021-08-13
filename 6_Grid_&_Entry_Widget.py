from tkinter import *

def getvals():
    print(f"username : {uservalue.get()}")
    print(f"password : {passwordvalue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)


uservalue = StringVar()
passwordvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passwordentry = Entry(root, textvariable = passwordvalue)

userentry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()