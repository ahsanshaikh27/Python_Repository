# We can place an if inside another if.

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("you can enter the club")
    else:
        print("You Need an ID card")
else:
    print("You are not old enough")

# Output: you can enter the club
    
