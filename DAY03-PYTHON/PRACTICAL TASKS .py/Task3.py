# Create a password guessing loop — if user enters correct password, print "Access granted", warna repeat until correct.

correct_password = "aws123"
while True:
    pwd = input("Enter password: ") 
    if pwd == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect pawwsord. Try again")