from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("App")
root.geometry("700x500")


def Undo():
    print("Undo")


def Redo():
    print("Redo")


def Cut():
    print("Cut")


def Copy():
    print("Copy")


def Paste():
    print("Paste")


def Find_Replace():
    print("Find & Replace")


def New_File():
    print("New File")


def Open_Folder():
    print("Open Folder")


def Open_File():
    print("Open File")


def function1():
    print("Go to File")


def Save():
    print("Save")


def Save_As():
    print("Save As")


def Print():
    print("Print")


def Help():
    print("Help")
    tmsg.showinfo("Help", "Please contact administrator for Help")


def Exit():
    print("Exit")
    a = tmsg.askquestion("Exit", "Do you wanr to exit")
    if a == "yes":
        root.quit()


filemenu = Menu(root)
m1 = Menu(filemenu, tearoff=0)

m1.add_command(label="New File", command=New_File)
m1.add_separator()
m1.add_command(label="Open Folder", command=Open_Folder)
m1.add_command(label="Open File", command=Open_File)
m1.add_separator()
m1.add_command(label="Save", command=Save)
m1.add_command(label="Save as", command=Save_As)
m1.add_separator()
m1.add_command(label="Print", command=Print)
root.config(menu=filemenu)
filemenu.add_cascade(label="File", menu=m1)

m2 = Menu(filemenu, tearoff=0)

m2.add_command(label="Undo", command=Undo)
m2.add_command(label="Redo", command=Redo)
m2.add_separator()
m2.add_command(label="Cut", command=Cut)
m2.add_command(label="Copy", command=Copy)
m2.add_command(label="Paste", command=Paste)
m2.add_separator()
m2.add_command(label="Find & Replace", command=Find_Replace)
root.config(menu=filemenu)
filemenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(filemenu, tearoff=0)
m3.add_command(label="Help", command=Help)
filemenu.add_cascade(label="Help", menu=m3)
root.config(menu=filemenu)

m4 = Menu(filemenu, tearoff=0)
m4.add_command(label="Exit", command=Exit)
filemenu.add_cascade(label="Exit", menu=m4)
root.config(menu=filemenu)
root.mainloop()
