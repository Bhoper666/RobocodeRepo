import tkinter as tk

def buttonpress():
    lbl.config(text='Button pressed!', font=('Times New Roman', 14, 'bold'))

root = tk.Tk()
root.title("My Window")
root.geometry("500x200")

lbl = tk.Label(root, text="Hello World!", font=('Arial', 16, 'bold italic'))
lbl.pack()

butt = tk.Button(root, text='press me Uwu', command=buttonpress)
butt.pack()

root.mainloop()
