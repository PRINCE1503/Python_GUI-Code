from tkinter import *

root = Tk()
root.title("Events Handling")
root.geometry("400x300")


def Click(event):
    print(f"Clicked at ({event.x},{event.y})")


widget = Button(root, text="Click")
widget.pack()

widget.bind("<Button-1>", Click)
widget.bind("<Double-1>", quit)
root.mainloop()
