import tkinter as tk
root=tk.Tk()              # Tk is a class ,root=our window object

root.title("Welcome")
root.geometry("400x300")
label=tk.Label(root,text="Enter Password")
label.pack()   #geometry manager
name_entry=tk.Entry(root,show="*")
name_entry.pack()
button=tk.Button(root,text="login")
button.pack()

root.mainloop()
