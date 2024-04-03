# To swap the value of two variables  
# we will user third variable which is a temporary variable 

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

print("Before Swap")
print(f"a = {a}, b = {b}")
temp = a
a = b
b = temp

print("\nAfter swap")
print(f"a = {a}, b = {b}")
