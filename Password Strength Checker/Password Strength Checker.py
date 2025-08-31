
password = input("Enter your password: ")

length = len(password)

if length < 4:
    print("Password is too weak ")
elif length < 8:
    print("Password is weak ")
else:
    print("Password is strong ")