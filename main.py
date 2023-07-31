from tkinter import *

window = Tk()
window.minsize(width=200,height=100)
window.config(padx=30, pady=20)
window.title("miles to kilometer")


entry = Entry(width=10)
entry.grid(row=1, column=5)



label = Label(text="miles")
label.grid(column=6,row=1)


label = Label(text="is equal to")
label.grid(column=2,row=2,padx=5,pady=5)


label = Label(text="KM")
label.grid(column=7,row=2,padx=5,pady=5)

def click():
    new= entry.get()
    new_num = int(new)
    new_value = round(new_num * 1.6,2)
    label.config(text=new_value)

label = Label(text=0)
label.grid(column=6,row=2,padx=5,pady=5)


button = Button(text="Calculate",command=click)
button.grid(column=6, row=3,padx=5,pady=5)






window.mainloop()