# Find the Factorial of any n number using recursion.

def function(n):
    if n == 1 or n == 0:
        return 1
    return n * function(n-1)

n = int(input("Enter the number : "))
f = function(n)
print("The factorial of " + str(n) + " is : " + str(f))