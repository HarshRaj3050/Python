# To swap the value of two variables. We can use the comma operator. 
# We do not need to use a third variable for swapping the values of two variables for this method

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

print("Before Swap")
print(f"a = {a}, b = {b}")

a, b = b, a

print("\nAfter swap")
print(f"a = {a}, b = {b}")