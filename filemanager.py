from pathlib import Path


path = str(Path.home()) + "\documents\gptkey.txt"


def searchKey():
    # If the key has already been given, it has been saved in the path below.
    try:
        with open(path, "r") as file:
            line = file.read()
            organ = line[:28]
            key = line[28:]
            return organ, key
    except:
        return "Organ not found", "Key not found"

def saveKey(organ, key):
    # Saves the given key to C:\user\documents in gptkey.txt
    with open(path, "w") as file:
        file.write(f'{organ}{key}')