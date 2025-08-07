
birth_year = int(input("Enter your birth year: "))

current_year = 2025

age = current_year - birth_year

print("Your age is", age, "years.")

if (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0):
    print("You were born in a leap year ")
