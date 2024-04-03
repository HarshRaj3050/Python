# Write a recursive function to calculate the sum of first n natural numbers.

def function(n):
    if n == 0 or n == 1:
        return 1
    return n + function(n-1)

n = int(input("Enter the Number : "))
sum = function(n)
print("The sum of " + str(n) + "natural number is : " + str(sum))