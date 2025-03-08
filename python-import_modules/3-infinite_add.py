#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    for arg in sys.argv[1:]:
        tot = sum(int(arg))
        print(tot)
