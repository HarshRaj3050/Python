# WAP to display the greatest between two given number

num1 = int(input("Enter the Number : "))
num2 = int(input("Enter the Number : "))
if(num1 > num2):
    print("First Number is Greater")
elif(num2 > num1):
    print("Second Number is Greater")
else:
    print("Both Number is Same")