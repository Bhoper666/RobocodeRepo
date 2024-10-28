import tkinter as tk

root = tk.Tk()
root.title('The window!')
root.geometry('400x300')

l1 = tk.Label(root, text='Hello World!', font=('Times New Roman', 16, 'bold italic'))
l1.pack()

b1 = tk.Button(root, text='Button', command=root.destroy)
b1.pack()

root.mainloop()
