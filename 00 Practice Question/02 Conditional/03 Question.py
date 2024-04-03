# WAP to display the greatest among the three number

num1 = int(input("Enter the Number : "))
num2 = int(input("Enter the Number : "))
num3 = int(input("Enter the Number : "))
if(num1 > num2):
    if(num1 > num3):
        print("First Number is Greater")
    else:
        print("Third Number is Greater")
else:
    if(num2 > num3):
        print("Second Number is Greater")
    else:
        print("Third Number is Greater")
