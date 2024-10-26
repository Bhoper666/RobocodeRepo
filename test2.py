import tkinter as tk
from tkinter import ttk

def buttonpress():
    lbl.config(text='Button pressed!', font=('Times New Roman', 14, 'bold'))
    root.config(bg='cyan')

def revertback():
    lbl.config(text='Hello World!', font=('Arial', 16, 'bold italic'))
    root.config(bg='#f0f0f0')

root = tk.Tk()
root.title("My Window")
root.geometry("500x200")

lbl = ttk.Label(root, text="Hello World!", font=('Arial', 16, 'bold italic'))
lbl.pack()

butt = ttk.Button(root, text='press me Uwu', command=buttonpress)
butt.pack()

butt2 = ttk.Button(root, text='revertback', command=revertback)
butt2.pack()

root.mainloop()
