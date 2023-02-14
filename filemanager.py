from pathlib import Path


path = str(Path.home()) + "\documents\gptkey.txt"


def searchKey():
    # If the key has already been given, it has been saved in the path below.
    try:
        with open(path, "r") as file:
            key = file.read()
            return key
    except:
        return "Key not found"

def saveKey(key):
    # Saves the given key to C:\user\documents in gptkey.txt
    with open(path, "w") as file:
        file.write(key)