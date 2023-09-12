# Find the Factorial of any n number using recursion.

def factorial(n):
    i = 1
    fact = 1
    while(i <= n):
        fact = fact * i
        i = i + 1
    return fact

num = int(input("Enter the number : "))
fact = factorial(num)
print(f"Factorial of {num} is : {fact}")