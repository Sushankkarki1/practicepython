# while True:
name = input("Enter your name: ")

if name.lower() == "sushank":
    birth_year = int(input("Enter your year of birth (AD): "))

    age = 2026 - birth_year

    print("Your age is " + str(age))

    if age < 25:
        print("You have time.")
    else:
        print("You don't have much time.")

# break
    
else:
    print("Enter again")