from tkinter import *
from PIL import Image, ImageTk

a_root = Tk()

a_root.geometry("290x400")
a_root.minsize(290,400)
a_root.maxsize(290,400)


image = Image.open("a.jpg")
photo = ImageTk.PhotoImage(image)

a_labl = Label(image=photo)
a_labl.pack()
a_root.mainloop()


