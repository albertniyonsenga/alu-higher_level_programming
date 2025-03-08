#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.arg[1:]
    arg_len = len(argv)
    for arg in argv:
        if arg_len == 0:
            print("0 arguments.")
        elif arg_len > 1:
            print(f"{arg_len} arguments:")
        else:
            print(f"{arg_len} argument:")

        for i, arg in enumerate(argv, 1):
            print(f"{i}: {arg}")
