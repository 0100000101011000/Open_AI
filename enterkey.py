import tkinter as tk
from tkinter import messagebox
from openai_request import testRequest

class enterKey(tk.Tk):
  

    def __init__(self):

        tk.Tk.__init__(self)
        self.label = tk.Label(self, text="Dein API-Key:")    
        self.input = tk.Entry(self)
        self.input.configure(width=100)
        self.button = tk.Button(self, text="Übernehmen", command=self.getKey)
        self.label.pack()
        self.input.pack()
        self.button.pack()

    def getKey(self):
        self.key = self.input.get()
        if testRequest(self.key) == "Valid key":
            self.destroy()
        else:
            messagebox.showerror(title="Error",message="Ungültiger Key!")



