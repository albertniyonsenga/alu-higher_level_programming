#!/usr/bin/python3
import hidden_4

def hidden():
    names = dir(hidden_4)
    for name in names:
        if not name.startwith("__"):
            print(name)

if __name__ == "__main":
    hidden()
