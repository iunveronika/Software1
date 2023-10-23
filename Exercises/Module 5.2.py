numbers = []

while True:
    num = input("Enter a number (or press Enter to quit): ")
    if not num:
        break
    numbers.append(float(num))

numbers.sort(reverse=True)
print(numbers[:5])
