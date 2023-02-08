from enterkey import enterKey

def testfunc():
    enterkey = enterKey()
    enterkey.mainloop()
    key = enterkey.key
    return key

key = testfunc()

print(key)