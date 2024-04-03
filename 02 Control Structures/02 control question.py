''' Write a python program to display the result such as distinction, first class,
    second class, pass or fail based on the marks entered by the user. '''

print('''----Result----
Marks 81-100 = First class
Marks 61-80 = Second class
Marks 41-60 = Pass
Marks 00-40 = Fail\n\n''')

marks = int(input("Enter your Marks : "))
if(marks >= 81 and marks <= 100):
    print("Your marks is : First Class")
elif(marks >= 61 and marks <= 80):
    print("Your marks is : Second Class")
elif(marks >= 41 and marks <= 60):
    print("Your marks is : Pass")
elif(marks >= 0 and marks <= 40):
    print("Your marks is : Fail")
else:
    print("Enter Valid marks")
