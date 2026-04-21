a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a>b and a>c :
    print("greatest number:",a)
elif b>c and b>a :
    print("greatest number:",b)
else:
    print("greatest number:",c)        