airports = {}

while True:
    choice = input("Do you want to (1) enter a new airport, (2) fetch information, or (3) quit? ")

    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ")
        name = input("Enter the name of the airport: ")
        airports[icao_code] = name
    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport you want information for: ")
        if icao_code in airports:
            print(airports[icao_code])
        else:
            print("No information found for the given ICAO code.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
