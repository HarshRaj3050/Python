# Find the Factorial of any n number using recursion.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter the number : "))
fact = factorial(num)
print(f"The Factorial of {num} is : {fact}")