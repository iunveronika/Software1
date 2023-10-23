def inches_to_cm():
    while True:
        user_input = input("Enter inches to convert to centimeters: ")

        inches = float(user_input)

        if inches < 0:
            break

        print(inches * 2.54)

inches_to_cm()