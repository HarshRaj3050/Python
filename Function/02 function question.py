# Write a python program using function to convert celsius to fahrenheit.

def ferh(cel):
    return ((cel * (9/5)) + 32)
cel = int(input("Enter the celsius values of convert fahrenheit : "))
fahrenheit = ferh(cel)
print(str(cel) + " celsius values = " + str(fahrenheit) + "fahrenheit values")