# Find the Factorial of any n number using recursion.

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter the number : "))
fact = factorial(num)
print(f"Factorial of {num} is : {fact}")