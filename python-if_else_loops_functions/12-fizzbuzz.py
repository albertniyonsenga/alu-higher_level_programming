#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 100):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"

        print("{}".format(i), end=" ")
