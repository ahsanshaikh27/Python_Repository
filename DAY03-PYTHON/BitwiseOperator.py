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