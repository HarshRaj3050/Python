# Write a program using function to find the greatest of three number.

def function(num1, num2, num3 ):
    if num1 > num2:
        if num1 > num3:
            return 1
        else:
            return 3
    else:
        if num2 > num3:
            return 2
        else:
            return 3

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

maximum = function(a,b,c)
if maximum == 1:
    print("First number is greater, the number is : " + str(a))
elif maximum == 2:
    print("Second number is greater, the number is : " + str(b))
else:
    print("third number is greater, the number is : " + str(c))