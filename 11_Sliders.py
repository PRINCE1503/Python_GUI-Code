from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("1200x200")


def Credit():
    print(f"You have ben Credited {slider2.get()} $ from your account!")
    tmsg.showinfo(
        "Amount Credited",
        f"You have been Credited {slider2.get()} $ from your account!",
    )


Label(root, text="Select Your Age", font="Helvetica 10").pack(side=TOP, anchor="w")
slider1 = Scale(root, from_=0, to=90)
slider1.set(18)
slider1.pack(side=LEFT, anchor="nw", fill=Y)

Label(root, text="How much $ you want to withdraw ?", font="times 12").pack()
slider2 = Scale(root, from_=0, to=250, orient=HORIZONTAL, tickinterval=10)
slider2.set(50)
slider2.pack(fill=X)
Button(root, text="Withdraw", font="times 12 bold", command=Credit).pack(
    side=BOTTOM, pady=10
)
root.mainloop()
