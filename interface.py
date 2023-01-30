import tkinter as tk
from GradientFrame import GradientFrame

def gpt_window():

  root = tk.Tk()
  root.title("AskGPT")

  gf = GradientFrame(root, colors = ("#FFFFFF", "#34eb74"), width = 800, height = 600)
  gf.config(direction = gf.top2bottom)
  gf.pack()

  label = tk.Label(gf, text="Frag etwas:",font=("Arial",12),background="#FFFFFF",foreground="#000000")
  label.pack(pady=20)

  askbox = tk.Text(gf, width=50, height=6)
  askbox.pack(pady=5)

  button = tk.Button(gf, text="Tell me!",font=("Arial",12),padx=15)
  button.pack(pady=20,padx=50)

  answerebox = tk.Text(gf, width=50, height=6)
  answerebox.configure(state="disabled")
  answerebox.pack(pady=50,padx=50)

  root.mainloop()
