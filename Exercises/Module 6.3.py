def gallons_to_liters(gallons):
    return gallons * 3.78541

while True:
    gallons = float(input("Enter the quantity of gasoline in American gallons: "))
    if gallons < 0:
        break
    liters = gallons_to_liters(gallons)
    print(f"{liters: .2f}")
