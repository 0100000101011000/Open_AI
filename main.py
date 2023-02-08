from interface import GptWindow
from openai_request import request_gpt
import tkinter as tk

class KeyAsk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        


def keyAsk():


def searchKey():
    try:
        with open("C:/gptkey/gptkey.txt", "r") as file:
            key = file.read()
            return key
    except:
        key = keyAsk()

key = searchKey()

root = GptWindow(color1="#7657e3", color2="#ffa247", key=key, aFunction=request_gpt)
root.mainloop()