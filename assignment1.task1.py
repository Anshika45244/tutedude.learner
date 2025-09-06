# Task 1: Perform Basic Mathematical Operations

#taking input from user

num1 = float(input("Enter the first number: "))
num2 = float (input("enter the second number: "))

 #perform operation
addition= num1 + num2
subtraction = num1-num2
multiplication = num1*num2
if num2!=0:
    division = num1/num2
else:
    division ="undefined "
#display result
print("\nResult:")
print(f"addition:{addition}")
print(f"subtraction:{subtraction}")
print(f"multiplication:{multiplication}")
print(f"division:{division}")


