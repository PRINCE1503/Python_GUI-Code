from tkinter import *


def Add_Item():
    global i
    lbx.insert(ACTIVE, f"item {i}")
    i += 1


i = 2

root = Tk()
root.geometry("400x300")
root.title("List Box")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "item 1")

Button(root, text="Add Item", command=Add_Item).pack()
root.mainloop()
