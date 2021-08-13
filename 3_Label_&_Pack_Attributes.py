from tkinter import *

# Label Attributes
root = Tk()
root.geometry("444x233")
root.title("-- My -- GUI --")
title_label = Label(
    text="This GUI made by Prince Padmani",
    bg="purple",
    fg="white",
    padx=20,
    pady=20,
    font=("comicsansms", 20, "italic", "bold"),
    borderwidth=4,
    relief=SOLID,
)

title_label.pack(side=BOTTOM,anchor="se",fill=X,padx=25,pady=25)

root.mainloop()