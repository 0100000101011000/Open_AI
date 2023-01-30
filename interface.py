import tkinter as tk


root = tk.Tk()
root.title("AskGPT")
root.minsize(600,400)
root.configure(background="#77f296")

label = tk.Label(root, text="Frag etwas",font=("Arial",12),background="#77f296",foreground="#FFFFFF")
label.pack()

askbox = tk.Text(root, width=30, height=6)
askbox.pack(pady=5)

button = tk.Button(root, text="Tell me!",font=("Arial",12),padx=15)
button.pack(pady=10)

answerebox = tk.Text(root, width=30, height=6)
answerebox.configure(state="disabled")
answerebox.pack()





root.mainloop()
