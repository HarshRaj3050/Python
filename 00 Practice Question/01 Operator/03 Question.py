# WAP to convert temperature given in Fahrenheit into degree Celsius.

f = float(input("Enter the Fahrenheit = "))
c = ((f-32)*5)/9
print(f"{f} Fahrenheit = {c:.1f} Celsius")