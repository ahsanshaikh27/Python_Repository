# Condition: age > 21 and salary > 25000

age = int(input("Enter your age: "))    
salary = int(input("Enter You monthly salary: "))   

if age > 21 and salary > 25000:
    print("You are eligible for loan.")
else:
    print("Sorry, you are not eligible for loan.")