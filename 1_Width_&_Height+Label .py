from tkinter import *

a_root = Tk()
# Width & Height
a_root.geometry("350x125")

a_root.minsize(400, 200)
a_root.maxsize(700, 350)

b_root = Label(text="Welcome to Python GUI(Graphic User Interface)")
b_root.pack()

a_root.mainloop()
