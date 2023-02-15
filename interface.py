import tkinter as tk
from GradientFrame import GradientFrame
from enterkey import EnterKeyWindow


class GptWindow(tk.Tk):

    """"""

    def noFunction(*args):
        return "Function is missing"

    def __init__(self, color1="#FFFFFF", color2="#000000", key="not telled", aFunction=noFunction):

        self.key = key

        tk.Tk.__init__(self)
        self.title("AskGPT")

        self.aFunction = aFunction
        self.iconbitmap("icon.ico")
        
        #Sets the backgroundcolor for the main window
        self.gf = GradientFrame(self, colors = (color1, color2), width = 800, height = 600)
        self.gf.config(direction = self.gf.top2bottom)
        self.gf.pack()

        self.label = tk.Label(self.gf, text="Ask GPT!",font=("Terminal",14,"bold"),background="#7657e3",foreground="#FFFFFF")
        self.label.pack(pady=20)

        self.askbox = tk.Text(self.gf, width=50, height=6)
        self.askbox.configure(font=12)
        self.askbox.pack(pady=5)

        self.button = tk.Button(self.gf, text="Tell me!",font=("Terminal",12),padx=15, command=self.buttonCommand)
        self.button.pack(pady=20,padx=50)
        

        self.answerebox = tk.Text(self.gf, width=50, height=6)
        self.answerebox.configure(state="disabled",font=12)
        self.answerebox.pack(pady=50,padx=50)

        if self.key == ("Key not found" or "not telled"):
            self.keyAsk()


    def keyAsk(self):
        
        # Creats an instance of EnterKeyWindow as enter_a_key which takes the key
        # as an user input. keyAsk waits for the enter_a_key window self closing,
        # what it will do after reseiving a valid key. Then it takes the key from
        # the still living object

        self.button.configure(state="disabled")
        
        self.enter_a_key = EnterKeyWindow()
        self.enter_a_key.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.enter_a_key.wait_window()
        # Here the code stops untill the enter_a_key window is destroyed
        self.key = self.enter_a_key.key

        self.button.configure(state="normal")


    def on_closing(self):
        # In case the user closes the window by himself
        self.enter_a_key.destroy()
        self.destroy()


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
