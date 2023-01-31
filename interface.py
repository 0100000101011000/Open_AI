import tkinter as tk
from GradientFrame import GradientFrame

def testfunc():
    print("TestFunktion")

class GptWindow(tk.Tk):

    def __init__(self, color1="#FFFFFF", color2="#000000",aFunction=0):

        self.aFunction = aFunction
        tk.Tk.__init__(self)
        self.title("Test")

        gf = GradientFrame(self, colors = (color1, color2), width = 800, height = 600)
        gf.config(direction = gf.top2bottom)
        gf.pack()

        label = tk.Label(gf, text="Frag etwas:",font=("Arial",12),background="#FFFFFF",foreground="#000000")
        label.pack(pady=20)

        askbox = tk.Text(gf, width=50, height=6)
        askbox.configure(font=12)
        askbox.pack(pady=5)

        button = tk.Button(gf, text="Tell me!",font=("Arial",12),padx=15, command=self.button_command)
        button.pack(pady=20,padx=50)

        answerebox = tk.Text(gf, width=50, height=6)
        answerebox.configure(state="disabled",font=12)
        answerebox.pack(pady=50,padx=50)

    def button_command(self):
        if self.aFunction != 0:
            self.aFunction()
        else:
            print("Funktion fehlt")

root = GptWindow(color2="#34eb74",aFunction=testfunc)
root.mainloop()
