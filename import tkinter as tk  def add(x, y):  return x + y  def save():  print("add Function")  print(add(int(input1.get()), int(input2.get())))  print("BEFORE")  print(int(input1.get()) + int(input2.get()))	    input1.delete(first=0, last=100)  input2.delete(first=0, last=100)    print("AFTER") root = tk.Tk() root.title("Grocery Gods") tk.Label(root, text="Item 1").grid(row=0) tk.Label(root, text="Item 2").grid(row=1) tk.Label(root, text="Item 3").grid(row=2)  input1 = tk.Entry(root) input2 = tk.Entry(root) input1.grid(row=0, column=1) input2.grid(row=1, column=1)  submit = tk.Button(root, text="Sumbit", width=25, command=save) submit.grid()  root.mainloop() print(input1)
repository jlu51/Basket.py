import tkinter as tk

def add(x, y):
 return x + y

def save():
 print("add Function")
 print(add(int(input1.get()), int(input2.get())))
 print("BEFORE")
 print(int(input1.get()) + int(input2.get()))	
 
 input1.delete(first=0, last=100)
 input2.delete(first=0, last=100)
 
 print("AFTER")
root = tk.Tk()
root.title("Grocery Gods")
tk.Label(root, text="Item 1").grid(row=0)
tk.Label(root, text="Item 2").grid(row=1)
tk.Label(root, text="Item 3").grid(row=2)

input1 = tk.Entry(root)
input2 = tk.Entry(root)
input1.grid(row=0, column=1)
input2.grid(row=1, column=1)

submit = tk.Button(root, text="Sumbit", width=25, command=save)
submit.grid()

root.mainloop()
print(input1)
