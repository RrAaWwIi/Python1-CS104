
age = int(input("Enter your age: "))
seat = input("Seat type (normal/premium): ")
weekend = input("Is it weekend? (yes/no): ")
student = input("Do you have a student card? (yes/no): ")

if age < 0 or age > 120:
    print("Please enter a valid age")
elif seat != "normal" and seat != "premium":
    print("Unknown seat type")
else:
    if seat == "normal":
        price = 220
    else:
        price = 350
    if age < 12 or age >= 60:
        price = price * 0.5
    if student == "yes" and weekend == "no":
        price = price * 0.8
    if weekend == "yes":
        price = price + 30
    print("Final ticket price:", price, "Baht")
