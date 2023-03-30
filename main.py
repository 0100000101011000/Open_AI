from interface import GptWindow
from openaiRequest import requestGpt
from filemanager import searchKey



organ, key = searchKey()

# Creats an instance of the main window
root = GptWindow(color1="#7657e3",
                 color2="#ffa247",
                 organ=organ,
                 key=key,
                 aFunction=requestGpt
)

root.mainloop()
