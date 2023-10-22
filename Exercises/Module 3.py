#1
zander = float(input("Enter the length of a zander in cm: "))
if zander>=42:
    print("Size limit is met")
else:
    print("Release the fish back into the lake.")
diffenence = 42-zander
if diffenence>0:
    print(f"The fish is {diffenence: .2f} centimeters below the size limit")

#2
cabinclass = input("Enter the cabin class of the cruise ship: ")
if cabinclass=="LUX":
    print("Upper-deck cabin with a balcony.")
elif cabinclass=="A":
    print("Above the car deck, equipped with a window.")
elif cabinclass=="B":
    print("Windowless cabin above the car deck.")
elif cabinclass=="C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

#3
gender = input("Enter biological gender: ")
hemoglobin = float(input("Enter hemoglobin value (g/l):"))
if gender=="female":
    if hemoglobin < 117:
        print("Hemoglobin is low")
    elif hemoglobin > 155:
        print("Hemoglobin is high")
    else:
        print("Hemoglobin is normal")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin is low")
    elif hemoglobin > 167:
        print("Hemoglobin is high")
    else:
        print("Hemoglobin is normal")

#4
year = int(input("Enter a year: "))
if (year % 100 == 0) and (year % 400 == 0):
    print("It is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("It is a leap year")
else:
    print("It is not a leap year")