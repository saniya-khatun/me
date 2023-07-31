# import tkinter 
# window = tkinter.Tk()
# window.title("my first GUI")
# window.minsize(width= 400,height=400)
# my_label = tkinter.Label(text="hello")
# my_label.pack()
# window.mainloop()


# def calculate(*args):
#     sum = 0
#     for value in args:
#         sum += value
#     return sum
# print(calculate(5,6,7,8,9))
    
def calculate(n,**kwargs):
    for(key,value) in kwargs.items():
        n+= kwargs[key]
        print(n)

calculate(5,a=5,b=6,c=9,d=2,e=5)


from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

# calls action() when pressed



button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# #Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=10, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=20, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect", listbox_used)
listbox.pack()


window.mainloop()



# window = Tk()
# window.title("aaa")
# window.minsize(width=400, height=300)

# def clicked():
#     print("i was clicked")
#     new_value = entry.get()
#     print(new_value)
#     label.config(text=new_value)



# label = Label(text="anish")
# label.pack()
# # label["text"] = "saniya"
# # label.config(text="neccccc")


# button = Button(text="click me",command=clicked)
# button.pack()

# entry = Entry(width=20)
# entry.pack()
# window.mainloop()








# def click():
#     print("I was clicked")
#     new_text = entry.get()
#     label.config(text = new_text)

# label = Label(text="Welcome!")
# label.grid(column=0, row=0)

# button = Button(text="press here",command=click)
# button.grid(column=1, row=1)

# entry = Entry(width=15)
# entry.grid(row=2, column=2)








