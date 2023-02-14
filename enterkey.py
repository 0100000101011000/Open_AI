import tkinter as tk
from tkinter import messagebox
from openai_request import testRequest
from filemanager import saveKey

class EnterKeyWindow(tk.Tk):
  

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
        # Takes the user inserted key and checks if it's valid
        self.key = self.input.get()

        if testRequest(self.key) == "Valid key":
            saveKey(self.key)
            self.destroy() # This will allow the calling function to continue

        else:
            # If not...
            messagebox.showerror(title="Error",message="Ungültiger Key!")
            self.focus_force()



