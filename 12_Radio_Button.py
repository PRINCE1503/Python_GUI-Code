from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x300")
root.title("Radio Button")


def Responce():
    tmsg.showinfo("Thanks for Responce!", f"You select {a.get()} as Gender")


a = StringVar()
a.set("Radio")
Label(
    root,
    text="Select Gender",
    font="lucida 16 bold italic underline",
    justify=LEFT,
    padx=14,
).pack()
radio = Radiobutton(
    root, text="Male", padx=14, variable=a, value="Male", font="helvetica 12"
).pack(anchor=W)
radio = Radiobutton(
    root, text="Female", padx=14, variable=a, value="Female", font="helvetica 12"
).pack(anchor=W)
radio = Radiobutton(
    root, text="Other", padx=14, variable=a, value="Other", font="helvetica 12"
).pack(anchor=W)

Button(text="Submit", font="hevetica 14 ", command=Responce).pack(padx=34)

root.mainloop()
