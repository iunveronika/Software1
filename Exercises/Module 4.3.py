numbers = []

while True:
    value = input("Enter a number (or press Enter to quit): ")

    if not value:
        break

    try:
        num = float(value)
        numbers.append(num)
    except ValueError:
        print("Please enter a valid number or press Enter to quit.")

if numbers:
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
else:
    print("No numbers were entered.")
