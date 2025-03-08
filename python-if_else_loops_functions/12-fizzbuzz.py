#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        i += 1
        if i % 3 == 0 or i % 5 == 0:
            i = "Fizzbuzz"

        print("{}".format(i), end=" ")
