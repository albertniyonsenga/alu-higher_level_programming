#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    for arg in args:
        tot = sum(int(arg))
        print(f"{tot}")
