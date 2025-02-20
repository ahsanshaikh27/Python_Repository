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