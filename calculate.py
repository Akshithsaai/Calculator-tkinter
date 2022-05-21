from tkinter import*
from turtle import bgcolor

root = Tk()
root.title("Simple calculator")

#entry widget
e=Entry(root,width=35,borderwidth=5,bg="white",fg="black")

e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
def click(number):
    e.insert(END,number)


#addition function
def add():
    number1=e.get()
    global n1
    global math
    math= "addition"
    n1=int(number1)
    e.delete(0,END)

#subtraction function
def sub():
    number1=e.get()
    global n1
    global math
    math= "subtraction"
    n1=int(number1)
    e.delete(0,END)

#multiplication function
def mul():
    number1=e.get()
    global n1
    global math
    math= "multiplication"
    n1=int(number1)
    e.delete(0,END)

#division function
def div():
    number1=e.get()
    global n1
    global math
    math= "division"
    n1=int(number1)
    e.delete(0,END)

#equal function
def equal():
    n2=int(e.get())
    e.delete(0,END)
    if math == "addition":
        e.insert(0,n1+n2)
    if math == "subtraction":
        e.insert(0,n1-n2)
    if math == "multiplication":
        e.insert(0,n1*n2)
    if math == "division":
        e.insert(0,n1/n2)

def clear():
    e.delete(0,END)



#defining  buttons
button_1= Button(root, text="1",padx=40 ,pady=20,command=lambda :click(1))
button_2= Button(root, text="2",padx=40 ,pady=20,command=lambda :click(2))
button_3= Button(root, text="3",padx=40 ,pady=20,command=lambda :click(3))
button_4= Button(root, text="4",padx=40 ,pady=20,command=lambda :click(4))
button_5= Button(root, text="5",padx=40 ,pady=20,command=lambda :click(5))
button_6= Button(root, text="6",padx=40 ,pady=20,command=lambda :click(6))
button_7= Button(root, text="7",padx=40 ,pady=20,command=lambda :click(7))
button_8= Button(root, text="8",padx=40 ,pady=20,command=lambda :click(8))
button_9= Button(root, text="9",padx=40 ,pady=20,command=lambda :click(9))
button_0= Button(root, text="0",padx=40 ,pady=20,command=lambda :click(0))
button_add=Button(root, text="+",padx=39,pady=20,command= add)
button_sub=Button(root, text="-",padx=41,pady=20,command= sub)
button_multiply=Button(root, text="*",padx=40,pady=20,command= mul)
button_divide=Button(root, text="/",padx=40,pady=20,command= div)

button_equal= Button(root, text="=",padx=90,pady=20,command= equal)
button_clear= Button(root, text="C",padx=40,pady=52,command= clear)


#showing buttons onto screen

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)
button_clear.grid(row=5,column=0,rowspan=2)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=5,column=2)

button_equal.grid(row=6,column=1,columnspan=2)



root.mainloop()