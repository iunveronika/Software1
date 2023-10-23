import math

def unit_price(diameter, price):
    area = math.pi * (diameter / 2) ** 2
    return price / area

diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))

diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))

unit_price1 = unit_price(diameter1, price1)
unit_price2 = unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")
