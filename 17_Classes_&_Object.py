from tkinter import *

class GUI (Tk):
    def __init__(self):
          super().__init__()
          self.geometry("500x350")


    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.statusbar=Label(self,textvar=self.var,relief=SUNKEN,anchor=W).pack(side=BOTTOM,fill="x")
    def click(self):
        print("Button Clicked")

    def button(self,inptext):
        Button(text=inptext,command=self.click).pack(pady=40)
if __name__ == '__main__':
    
    window=GUI()
    window.status()
    window.button("Click")
    window.mainloop()