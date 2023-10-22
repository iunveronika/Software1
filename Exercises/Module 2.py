#1
name = input("Enter your name: ")
print("Hello, " + name + "!")

#2
import math
pi=math.pi
circleradius = float(input('Please enter radius of a circle to calculate the area of circle: '))
circlearea = circleradius**2*pi
print(f"Area of the circle is: {circlearea: .2f}!")

#3
length = float(input("Please enter rectangle's length: "))
width = float(input("Please enter rectangle's width: "))
perimeter = 2 * length + 2 * width
area = length*width
print("Rectangle's perimeter is: ", perimeter)
print("Rectangle's area is: ", area)

#4
int1 = int(input("Enter first integer number: "))
int2 = int(input("Enter second integer number: "))
int3 = int(input("Enter third integer number: "))
intsum = int1 + int2 + int3
intproduct = int1 * int2 * int3
intaverage = intsum / 3
print("Sum of numbers is: ", intsum)
print("Product of the numbers is: ", intproduct)
print("Average of the numbers is: ", intaverage)

#5
#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.

import math
talentmass = float(input("Enter talents: "))
poundmass = float(input("Enter pounds: "))
lotmass = float(input("Enter lots: "))
talentsinpounds = talentmass * 20
totalpoundsinlots = (talentsinpounds + poundmass) * 32
totallotsingrams = (totalpoundsinlots + lotmass) * 13.3
kilograms = math.floor(totallotsingrams / 1000)
grams = totallotsingrams - kilograms * 1000
print(f"The weight in modern units: {kilograms: .2f} kilograms and {grams: .2f} grams.")

#6
import random
print("3 numbers for the combination lock: ", random.randint (0,9), random.randint (0,9), random.randint (0,9))
print("4 numbers for the combination lock: ", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))