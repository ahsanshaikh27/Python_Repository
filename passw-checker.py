correct_password = "aws123"
while True:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password. Try again.")
