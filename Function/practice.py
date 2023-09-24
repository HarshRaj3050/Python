# Write a python program using function to check if the enered year is leap year or not.

def leap(year):
    if(year % 4 == 0 and year % 100 != 0):
        print("The Year is leap year")
    elif(year % 400 == 0):
        print("The year is leap year")
    elif(year % 100 == 0):
        print("The year is not leap year")
    else:
        print("The is Year is not leap year")

year = int(input("Enter the Year : "))
leap(year)