#Calculate Factorial Using a Function
a= int(input("enter a number : "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
return_factorial = factorial(a)
print("Factorial of n is : " ,return_factorial)
