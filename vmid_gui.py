from tkinter import *

root = Tk()
root.title("My Window")
root.geometry("640x480")

l1 = Label(root, text="Калькулятор Vсер. Copyright 2024 Herobrine Studios. All rights reserved.", font=('Arial', 12))
l1.pack()

def sum_of_fields():
    try:
        result = (float(e1.get()) + float(e2.get()) + float(e3.get())) / float(e4.get())
        l2.config(text=f'Vсер: {result} км/год')
    except ValueError:
        l2.config(text=' Введiть коректнi данi! ')

l1 = Label(root, text="Введiть l1: ")
l1.pack()
e1 = Entry(root, width=10)
e1.pack()
l2 = Label(root, text="Введiть l2: ")
l2.pack()
e2 = Entry(root, width=10)
e2.pack()
l3 = Label(root, text="Введiть l3: ")
l3.pack()
e3 = Entry(root, width=10)
e3.pack()  
l4 = Label(root, text="Введiть t: ")
l4.pack()
e4 = Entry(root, width=10)
e4.pack()

l2 = Label(root, text=" ", font=('Arial', 20, 'bold italic'))
l2.pack()

b1 = Button(root, text="Обчислити", command=sum_of_fields)
b1.pack()

root.mainloop()
