"""
import random

def roll_the_dice():
    dice = random.randint(1,6)
    return dice

rolls = 0
while roll_the_dice() != 6:
    rolls = rolls + 1
    print(roll_the_dice())
else:
    print("6")

"""

import random
def roll_the_dice(sides):
    dice = random.randint(1, sides)
    return dice

sides = int(input("Enter the number of sides: "))
rolls = 0
result = roll_the_dice(sides)

while result != sides:
    print(result)
    rolls = rolls + 1
    result = roll_the_dice(sides)

print(rolls, "times")







