# WAP to swap two numbers.

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
print("\n-----Before Swap-----")
print(f"First Number : {a} Second Number {b}")
temp = a
a = b
b = temp
print("\n-----After Swap-----")
print(f"First Number : {a} Second Number {b}")
