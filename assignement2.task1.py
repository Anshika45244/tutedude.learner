# Task 1: Check if a Number is Even or Odd

try:
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
