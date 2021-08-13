from tkinter import *

root = Tk()
root.geometry("305x40")
root.maxsize(305, 40)
root.minsize(305, 40)

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")


def Home():
    print("Go to Home")


def About():
    print("Go to About")


def Help():
    print("Go to Help")


def Print():
    print("Go to Print")


def FAQs():
    print("Go to FAQ section")


b1 = Button(frame, fg="red", text="Home", command=Home)
b1.pack(side=LEFT)
b1 = Button(frame, fg="red", text="About", command=About)
b1.pack(side=LEFT, padx=20)
b1 = Button(frame, fg="red", text="Help", command=Help)
b1.pack(side=LEFT)
b1 = Button(frame, fg="red", text="Print", command=Print)
b1.pack(side=LEFT, padx=20)
b1 = Button(frame, fg="red", text="FAQs", command=FAQs)
b1.pack(side=LEFT)
root.mainloop()
