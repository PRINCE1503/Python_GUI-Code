from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Scroll Bar")

a = Scrollbar(root)
a.pack(fill=Y, side=RIGHT)

listbox = Listbox(root, yscrollcommand=a.set)
for i in range(100):
    listbox.insert(END, f"Item {i}")
listbox.pack(fill=BOTH, padx=35, pady=35)
a.config(command=listbox.yview)
root.mainloop()
