def inches_to_centimeters(inches):
    return inches * 2.54

while True:
    try:
        value = float(input("Enter a value in inches: "))
        if value < 0:
            break
        cm = inches_to_centimeters(value)
        print(f"{value} inches is {cm} centimeters.")
    except ValueError:
        print("Please enter a valid number.")

print("Program ended.")
