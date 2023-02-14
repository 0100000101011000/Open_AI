import tkinter as tk
from GradientFrame import GradientFrame
from enterkey import enterKey


class GptWindow(tk.Tk):

    def noFunction(trash):
        return "Keine Funktion"

    def __init__(self, color1="#FFFFFF", color2="#000000", key="", aFunction=noFunction):

        self.key = key

        tk.Tk.__init__(self)
        self.title("AskGPT")

        self.aFunction = aFunction
        self.iconbitmap("C:/programming/Open_AI/icon.ico")

        gf = GradientFrame(self, colors = (color1, color2), width = 800, height = 600)
        gf.config(direction = gf.top2bottom)
        gf.pack()

        label = tk.Label(gf, text="Ask GPT!",font=("Terminal",14,"bold"),background="#7657e3",foreground="#FFFFFF")
        label.pack(pady=20)

        self.askbox = tk.Text(gf, width=50, height=6)
        self.askbox.configure(font=12)
        self.askbox.pack(pady=5)

        button = tk.Button(gf, text="Tell me!",font=("Terminal",12),padx=15, command=self.buttonCommand)
        button.pack(pady=20,padx=50)

        self.answerebox = tk.Text(gf, width=50, height=6)
        self.answerebox.configure(state="disabled",font=12)
        self.answerebox.pack(pady=50,padx=50)

        if self.key == "Key not found":
            self.keyAsk()

    def keyAsk(self):
        keyask = enterKey()
        keyask.wait_window()
        self.key = keyask.key

    def buttonCommand(self):
        question = self.askbox.get("0.0", "end")
        answere = self.aFunction(question, self.key)
        if answere != "Invalid key":
            self.answerebox.configure(state="normal")
            self.answerebox.delete("0.0", "end")
            self.answerebox.insert("0.0", answere)
            self.answerebox.configure(state="disabled")
        else:
            self.keyAsk()
