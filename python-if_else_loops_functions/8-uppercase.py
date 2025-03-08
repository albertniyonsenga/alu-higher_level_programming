#!/usr/bin/python3
def uppercase(str):
    for text in str:
        if ord(text) >= 97 and ord(text) <=122:
            text = chr(ord(text) - 32)
            print(f"{}\n".format(text), end="")
