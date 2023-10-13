"""

print("Hello, Veronika!")

name = input("What is your name? ")
print(f"Hello, {name}!")

import math
radius = float(input("Radius of the circle: "))
area = math.pi * (radius**2)
print(f"Area = {area}")

length = float(input("Length of the rectangle: "))
width = float(input("Width of the rectangle: "))
perimeter = length*2 + width*2
area = length * width
print(f"Perimeter = {perimeter}")
print(f"Area = {area}")





number1 = int(input("Enter the first integer number: "))
number2 = int(input("Enter the second integer number: "))
number3 = int(input("Enter the third integer number: "))

sum = number1 + number2 + number3
product = number1 * number2 * number3
average = (number1 + number2 + number3)/3

print(f"The sum of numbers is: {sum}")
print(f"The product of product is: {product}")
print(f"The average of numbers is: {average:.2f}")


import random
number = random.sample([0, 1, 2, 3, 4, 5, 6], 3)
print(number)


#6
import random
print("3 numbers for the combination lock: ", random.randint (0,9), random.randint (0,9), random.randint (0,9))
print("4 numbers for the combination lock: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))



i = 1
while i < 11:
    print(i)
    i = i + 1


amount_greet = int(input("How many greetings do you want displayed? "))
greeting = 1
while greeting <= amount_greet:
    print("Good morning!")
    greeting = greeting + 1



command = input("Enter command: ")
while command != "stop":
    print("Executing: ", command)
    command = input("Enter command: ")
print("Execution is stopped")


"""
import random
dice1 = 0
dice2 = 0
rolls = 0

while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"The dice were rolled {rolls} times.")


number = int(input("Enter integer: "))
factorial = 1
for i in range (1, number+1):
    factorial = factorial * i
print(factorial)




