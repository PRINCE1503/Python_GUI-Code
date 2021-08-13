from tkinter import *

root = Tk()
root.title("Canvas Widget")
canvas_width = 800
canvas_height = 600
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 600, fill="red")
can_widget.create_line(0, 600, 800, 0, fill="red")

can_widget.create_rectangle(10, 0, 200, 100, fill="blue")

can_widget.create_text(400, 300, text="Python Tkinter", font="times 18 bold")

can_widget.create_oval(250, 60, 380, 100, fill="yellow")

root.mainloop()
