from interface import GptWindow
from openai_request import request_gpt

#34eb74

root = GptWindow(color1="#7657e3", color2="#ffa247", aFunction=request_gpt)
root.mainloop()