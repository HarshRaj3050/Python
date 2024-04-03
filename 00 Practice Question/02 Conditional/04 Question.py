''' WAP to calculate the grade of an employee depending upon the given basic salary.
    {Grade A for salary above 5000, B for salary more than 3000 and lesser than or equal
    to 5000 and C for salary lesser than or equal to 3000}'''

salary = int(input("Enter the basic Salary : "))
if(salary > 5000):
    print("Employee Grade : A")
elif(salary <= 5000 and salary > 3000):
    print("Employee Grade : B")
else:
    print("Employee Grade : C")
