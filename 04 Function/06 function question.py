# Write a python program using function to check if the enered year is leap year or not.

def leap(year):
    if(year % 4 == 0 and year % 100 != 0):
        print(f"{year} is leap Year")
    elif(year % 400 == 0):
        print(f"{year} is leap Year")
    elif(year % 100 == 0):
        print(f"{year} is not leap Year")
    else:
        print(f"{year} is not leap Year")
year = int(input("Enter the year : "))
leap(year)
