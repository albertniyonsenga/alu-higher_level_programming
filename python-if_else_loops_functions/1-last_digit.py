#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
   digit = -digit
   print("Last digit of {} is {} and is ".format(number, digit), end="")

   if digit > 5:
      print("Last digit of {} is {} and is greater than 5".format(number, digit), end="")

   elif digit == 0:
        print("Last digit of {} is {} and is {}".format(number, digit), end="")

   else:
       print("Last digit of {} is {} and is less than 6 and not 0".format(number, digit), end="")
