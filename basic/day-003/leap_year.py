year = int(input("Enter with a year: "))

if year <= 1582:
    print("Year must be greater than 1582 - the first year of Gregorian calendar.")

elif year % 4 == 0:

    if year % 100 == 0:
        if  year % 400 == 0:
            print(f"Year {year} is a leap year.")
        else:
            print(f"Year {year} it is NOT a leap year.")
    else:
        print(f"Year {year} is a leap year.")
else: 
    print(f"Year {year} it is NOT a leap year.")