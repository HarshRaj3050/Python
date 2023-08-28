''' Write a python program to display the result such as distinction, first class,
    second class, pass or fail based on the marks entered by the user. '''

print('''----Result----
Marks 81-100 = First class
Marks 61-80 = Second class
Marks 41-60 = Pass
Marks 00-40 = Fail\n\n''')

marks = int(input("Enter your Marks : "))
if(marks >= 81 or marks <= 100):
    print("First Class")
elif(marks >= 61 or marks <= 80):
    print("Second Class")
elif(marks >= 41 or marks <= 60):
    print("Pass")
elif(marks >= 0 or marks <= 40):
    print("Fail")
