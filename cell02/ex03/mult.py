#!/usr/bin/env python3

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

mult = first_number * second_number
print(first_number, "x", second_number, "=", mult)

if mult < 0:
    print("The result is negative.")
elif mult == 0:
    print("The result is positive and negative.")
else:
    print("The result is positive.")
