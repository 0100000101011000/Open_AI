from GradientFrame import GradientFrame
import tkinter as tk

root = tk.Tk()
gf = GradientFrame(root, colors = ("yellow", "black"), width = 800, height = 600)
gf.config(direction = gf.top2bottom)
gf.pack()

label = tk.Label(gf, text="Frag etwas",font=("Arial",12),background="#77f296",foreground="#FFFFFF")
label.pack()

button = tk.Button(gf, text="Tell me!",font=("Arial",12),padx=15)
button.pack(pady=100)

root.mainloop()