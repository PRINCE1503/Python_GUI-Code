from tkinter import *

root = Tk()
root.title("Text Editor")
root.geometry("650x335")
f1 = Frame(root, bg="light blue", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)
l = Label(f1, text="This was made by Python")
l.pack(pady=140)
f2 = Frame(root, borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)
l = Label(f2, text="Welcome to Text Editor", font="Helvetica 18 bold italic", fg="red")
l.pack()

root.mainloop()
