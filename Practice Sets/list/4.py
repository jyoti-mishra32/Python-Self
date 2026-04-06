# Count how many even numbers are present in a list
numbers = [2,3,4,5,6,7,8]
count=len([i for i in numbers if i % 2 == 0])
print("Even numbers count:",count)