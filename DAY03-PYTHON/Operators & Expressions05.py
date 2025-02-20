# Arithmetic Operators
a = 10
b = 3

print(a + b)  # 13 (Addition)
print(a - b)  # 7 (Subtraction)
print(a * b)  # 30 (Multiplication)
print(a / b)  # 3.33 (Division)
print(a % b)  # 1 (Modulus)
print(a ** b)  # 1000 (10^3) (Exponentiation)
print(a // b)  # 3 (Floor division) 

# Comparison Operators

x = 10
y = 5

print(x == y)  # False (Equal)
print(x != y)  # True (Not equal)
print(x > y)   # True (Greater than)
print(x < y)   # False  (Less than)
print(x >= y)  # True (Greater than or equal to)
print(x <= y)  # False (Less than or equal to)

# Logical Operators
 # ( operater and )	(Returns True if both conditions are True)	: Example (5 > 3) and (10 > 5) → True
 
  
print(a > b and b > a)  # True

# ( operater or )	(Returns True if one of the conditions is True)	: Example (5 > 3) or (10 < 5) → True
 
print(a > b or b < a)   # True

# ( operater not )	(Reverse the result, returns False if the result is True)	: Example not(5 > 3) → False

print(not(a > b))  # False

# Assignment Operators Used to assign values to variables.
#  Operator	Example	   Equivalent to
#  =	     x = 5	         x = 5
#  +=	     x += 3	         x = x + 3
#  -=	     x -= 3	         x = x - 3  
#  *=	     x *= 3	         x = x * 3
#  /=	     x /= 3	         x = x / 3
#  %=	     x %= 3	         x = x % 3
#  //=	     x //= 3	     x = x // 3
#  **=	     x **= 3	     x = x ** 3

x = 10

x += 5  # x = x + 5
print(x)  # 15

x *= 2  # x = x * 2
print(x)  # 30

#  Bitwise Operators Operate at the binary level.
#  Operator	    Description    Example	 
# &	               AND	      5 & 3 → 1(0101 & 0011 = 0001)
# ^              XOR	      5 ^ 3 → 6(0101 ^ 0011 = 0110)
# ~               NOT	      ~5 → -6(~0101 = 1010)
# <<	           Left shift	  5 << 1 → 10(0101 << 1 = 1010)
# >>	           Right shift	  5 >> 1 → 2(0101 >> 1 = 0010)

a = 5  # 0101
b = 3  # 0011
                      #Output
print(a & b)           # 1
print(a | b)           # 7
print(a ^ b)           # 6
print(~a)              # -6
print(a << 1)          # 10
print(a >> 1)          # 2

#: Identity Operators Used to compare objects, not if they are equal, but if they are actually the same object, with the same memory location.

#  Operator	 Description	 Example
#  is	     Returns True if both variables are the same object	: Example x is y
#  is not	 Returns True if both variables are not the same object	: Example x is not y

#Example

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True (Same object)
print(x is z)  # False (Different objects)
print(x == z)  # True (Same values)


#  Membership Operators Used to test if a sequence is presented in an object.

#  Operator	 Description	 Example
#  in	     Returns True if a sequence with the specified value is present in the object	: Example x in y
#  not in	 Returns True if a sequence with the specified value is not present in the object	: Example x not in y

#Example
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)  # True
print("grape" not in fruits)  # True


