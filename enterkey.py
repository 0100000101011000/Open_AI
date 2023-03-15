import tkinter as tk
from tkinter import messagebox
from openaiRequest import testRequest
from filemanager import saveKey

class EnterKeyWindow(tk.Tk):
  

    def __init__(self):

        tk.Tk.__init__(self)
        self.organLabel = tk.Label(self, text="Organisationscode:")
        self.keyLabel = tk.Label(self, text="Dein API-Key:")
        self.keyInput = tk.Entry(self)
        self.organInput = tk.Entry(self)
        self.keyInput.configure(width=100)
        self.organInput.configure(width=70)
        self.button = tk.Button(self, text="Übernehmen", command=self.getKey)
        self.organLabel.pack()
        self.organInput.pack()
        self.button.pack()
        self.keyLabel.pack()
        self.keyInput.pack(padx=20,pady=5)
        self.resizable(width=False,height=False)
        


    def getKey(self):
        # Takes the user inserted key and checks if it's valid
        self.organ = self.organInput.get()
        self.key = self.keyInput.get()

        if testRequest(self.organ, self.key) == "Valid key":
            saveKey(self.organ, self.key)
            self.destroy() # This will allow the calling function to continue

        else:
            # If not...
            messagebox.showerror(title="Error",message="Ungültiger Key!")
            self.focus_force()



