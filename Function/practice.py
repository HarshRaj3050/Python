# Find the Factorial of any n number using recursion.

def factorial(num):
    if num == 0 or num == 1 :
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter the number : "))
fact = factorial(num)
print(f"The Factorial of {num} is : {fact}")