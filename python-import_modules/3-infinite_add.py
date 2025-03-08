#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    for args in args:
        tot = sum(int(args))
        print(f"{tot}")
