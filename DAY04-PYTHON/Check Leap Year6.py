year = int(input("Enter A Year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap Year")
    
else:
    print(year, " is not a leap Year")