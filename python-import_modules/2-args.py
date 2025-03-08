#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg = sys.argv[1:]
    arg_len = len(arg)
    for argu in arg_len:
        if argu == 0:
            print("0 arguments.")
        elif argu > 1:
            print(f"{arg_len} arguments:")
        else:
            print(f"{arg_len} argument:")

        for i, argum in enumerate(arg, 1):
            print(f"{i}: {argum}")
