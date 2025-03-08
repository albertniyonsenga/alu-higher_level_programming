#!/usr/bin/python3
def uppercase(str):
    word = ""
    for text in str:
        if 'a' <= text <= 'z':
            word += chr(ord(text) - 32)
        else:
            word += text

    print("{}".format(word))
