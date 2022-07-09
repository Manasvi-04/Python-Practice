from tkinter import *


def converter():
    in_miles = int(input.get())
    in_kilo = in_miles/0.62
    ans.config(text=int(in_kilo))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=150, height= 100)
window.config(padx=20, pady=20)

lable_0 = Label()
lable_0.grid()

input = Entry(text="0", width=8)
input.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)


ans = Label(text="0")
ans.grid(column=1, row=1)

kilometer = Label(text="Km")
kilometer.grid(column=2, row=1)

calculate = Button(text="Convert", command=converter)
calculate.grid(column=1, row=2)

window.mainloop()