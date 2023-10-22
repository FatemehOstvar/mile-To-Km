from tkinter import *

# Window

window = Tk()
window.title("Setareh")
window.minsize()
window.config(padx=30, pady=40)

milesLabel = Label(text="Miles")
milesLabel.grid(column=2, row=0)

XLabel = Label(text="0")
XLabel.grid(column=1, row=1)

isEqualLabel = Label(text="is equal to")
isEqualLabel.grid(column=0, row=1)

KmLabel = Label(text="Km")
KmLabel.grid(column=2, row=1)



# input
milesInput = Entry()
milesInput.grid(column=1, row=0)


def miles_to_km_convertor():
    XLabel.config(text=(float(milesInput.get())*1.609))


# Button
CalcButton = Button(text="Calculate", command=miles_to_km_convertor)
CalcButton.grid(column=1, row=2)

window.mainloop()
