import os

def check_website(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        print(host, "is up!")
    else:
        print(host, "is down.")

check_website("google.com")
check_website("aws.amazon.com")
