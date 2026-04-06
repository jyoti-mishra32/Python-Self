# Take marks as input and print grade.
marks = int(input("Enter marks:"))

if(marks >= 90):
  print("Grade A")
elif(marks >=75 and marks < 89 ):
  print("Grade B")
elif(marks >=50 and marks < 74):
  print("Grade C")
else:
  print("Fail")