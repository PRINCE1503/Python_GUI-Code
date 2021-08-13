from tkinter import *


def upload():
    status.set("Busy...")
    sbar.update()
    import time

    time.sleep(2)
    status.set("Ready ")


root = Tk()
root.geometry("500x400")
root.title("Status Bar")

status = StringVar()
status.set("Ready")
sbar = Label(root, textvariable=status, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack(pady=50)
root.mainloop()
