from tkinter import *

root = Tk()
root.geometry("500x400")
root.configure(bg="light blue")
root.title("Form")


def Info():
    print(f"Name : {namevalue.get()}")
    print(f"Phone : {phonevalue.get()}")
    print(f"Gender : {gendervalue.get()}")
    print(f"Emergency Contact : {emergencyvalue.get()}")
    print(f"Payment Method : {paymentmodevalue.get()}")
    if foodservicevalue.get() == 0:
        print("Prebook Meals : No")
    else:
        print("Prebook Meals : Yes")
    print("\n")
    with open("1_Form_Record.txt", "a") as f:
        if foodservicevalue.get() == 0:
            f.write(
                f"Name : {namevalue.get()}\nPhone : {phonevalue.get()}\nGender : {gendervalue.get()}\nEmergency Contact : {emergencyvalue.get()}\nPayment Method : {paymentmodevalue.get()}\nPrebool Meals : No\n------------------------------------------------------\n"
            )
        else:
            f.write(
                f"Name : {namevalue.get()}\nPhone : {phonevalue.get()}\nGender : {gendervalue.get()}\nEmergency Contact : {emergencyvalue.get()}\nPayment Method : {paymentmodevalue.get()}\nPrebool Meals : Yes\n------------------------------------------------------\n"
            )


Label(
    root,
    text="Welcome",
    font="comicsansms 20 bold italic underline",
    fg="blue",
    bg="light blue",
    pady=15,
).grid(row=0, column=3)


name = Label(root, text="Name", font="time", bg="light blue").grid(row=1, column=2)
phone = Label(root, text="Phone", font="time", pady=14, bg="light blue").grid(
    row=2, column=2
)
gender = Label(root, text="Gender", font="time", bg="light blue").grid(row=3, column=2)
emergency = Label(
    root, text="Emergency Contact", font="time", pady=14, bg="light blue"
).grid(row=4, column=2)
paymentmode = Label(root, text="Payment Mode", font="time", bg="light blue").grid(
    row=5, column=2
)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(
    root, textvariable=namevalue, bg="orange", fg="black", font="time"
).grid(row=1, column=3)
phoneentry = Entry(
    root, textvariable=phonevalue, bg="orange", fg="black", font="time"
).grid(row=2, column=3)
genderentry = Entry(
    root, textvariable=gendervalue, bg="orange", fg="black", font="time"
).grid(row=3, column=3)
emergencyentry = Entry(
    root, textvariable=emergencyvalue, bg="orange", fg="black", font="time"
).grid(row=4, column=3)
paymentmodeentry = Entry(
    root, textvariable=paymentmodevalue, bg="orange", fg="black", font="time"
).grid(row=5, column=3)

foodservice = Checkbutton(
    text="Want to prebook your meals?",
    font="time",
    variable=foodservicevalue,
    pady=10,
    bg="light blue",
).grid(row=6, column=3)

b1 = Button(text="Submit", font="Helvetica 12 bold", command=Info, pady=9).grid(
    row=7, column=3
)

root.mainloop()
