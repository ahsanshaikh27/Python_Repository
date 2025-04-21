# Linux user checker script

import os

user = os.getlogin()

if  user == "ubuntu":
    print("You are using EC2 default user.")
else:
    print("User is:",user)