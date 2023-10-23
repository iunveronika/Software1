def get_extremes():
    numbers = []

    while True:
        user_input = input("Enter a number (or press enter to quit): ")

        if not user_input:
            break

        if user_input.replace(".", "", 1).isdigit() or (
                user_input[0] == "-" and user_input[1:].replace(".", "", 1).isdigit()):
            numbers.append(float(user_input))
        else:
            print("Invalid input.")

    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))


get_extremes()
