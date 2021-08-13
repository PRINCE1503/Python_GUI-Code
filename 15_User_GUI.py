from tkinter import *

root = Tk()
root.geometry("350x230")
root.configure(bg="light blue")


def resize():
    print("Updating GUI...")
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")


root.title("Window Resizer")
Label(
    text="Window Resizer",
    font="lucida 20 bold underline",
    pady=14,
    bg="light blue",
    fg="red",
).grid(column=2)

Label(text="Width: ", font="lucida 14", bg="light blue").grid(
    row=1, column=1, padx=20, pady=8
)
Label(text="Height: ", font="lucida 14", bg="light blue").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width, bg="orange", font="time").grid(
    row=1, column=2
)
height_entry = Entry(root, textvariable=height, bg="orange", font="time").grid(
    row=2, column=2
)

Button(text="Apply", command=resize, pady=4, padx=4.7, font="helvetica 14 italic").grid(
    column=2, pady=20
)

root.mainloop()
