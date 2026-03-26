# Arithmatic operator
a = 5
b = 2

print(a + b)   # Sum
print(a - b)   # Difference
print(a * b)   # Multiply
print(a / b)   # Divide
print(a % b)   # Remainder
print(a ** b)  # Power

# Relational operators
a = 50 
b = 20

print(a == b)   # Eqaul to
print(a != b)   # Not equal to
print(a > b)    # Greater
print(a >= b)   # Greater than equal to
print(a < b)    # Less
print(a <= b)   # Less than equal to

# Assignment operators
num = 10
num = num + 10      # 10+10=20
print("num :", num)

num += 5
print("num :", num)

num -= 5
print("num :", num)

num *= 5
print("num :", num)

num /= 5
print("num :", num)

num %= 5
print("num :", num)

num **= 5
print("num :", num)

# Logical operators
print(not False)
print(not True) 

a = 50
b = 30
print(not (a > b))

val1 = True
val2 = True
print("and operator:",val1 and val2)

val1 = False
val2 = False
print("and operator:",val1 and val2)
print("OR operator:", val1 and val2)
print("OR operator:", (a == b) and (a > b))