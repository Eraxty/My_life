good_colleges = ["IIT", "NIT", "BITS", "MIT"]
branches = ["CS", "ECE", "Mechanical", "Aeronautical"]

college = input("Enter your college: ")
money = int(input("Enter how much money you have (INR): "))

if college in good_colleges:
    print("Congrats! You got into a good college.")
    print("Branches available:", branches)
    user_branch = input("Enter branch you chose: ")

    if user_branch == "CS":
        print("Path: Become an engineer, software developer, or AI expert.")
    elif user_branch == "Mechanical":
        print("Path: Work in F1, automotive engineering, or car design.")
    elif user_branch == "ECE":
        print("Path: Build robots, electronics, or work in IoT.")
    elif user_branch == "Aeronautical":
        print("Path: Aerospace engineering, rockets, drones.")
    else:
        print("Branch not recognized, try again next life.")

else:
    print("College not top-tier, alternative paths suggested.")
    pilot_choice = input("Do you want to become a pilot? (yes/no): ").lower()

    if pilot_choice == "yes":
        if money >= 1000000:
            print("You can afford pilot school. Fly high!")
        else:
            print("Money is insufficient for pilot school.")
            print("Alternate paths: Musician, game developer, climbing Everest, coding, or online freelancing.")
    else:
        print("Alternate paths: Musician, game developer, coding, online freelancing, or adventurous careers.")

print("Remember, life is full of if-else conditions. Choose wisely!")
