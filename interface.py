import tkinter as tk


root = tk.Tk()
root.title("Textbox GUI")

textbox1 = tk.Entry(root)
textbox1.pack()

textbox2 = tk.Entry(root)
textbox2.pack()

button = tk.Button(root, text="Show Text")
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
