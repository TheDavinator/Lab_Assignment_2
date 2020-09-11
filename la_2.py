def street_direction(street):
    if (street % 2 == 0):
        print("This street is eastbound.")
    else:
        print("This street is westbound.")

street = int(input("Put the street number wish to find the direction of here: "))
street_direction(street)