# WAP to swap two numbers without using third variable

a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
print("\n-----Before Swap-----")
print(f"First Number : {a} Second Number {b}")
a, b = b, a
print("\n-----After Swap-----")
print(f"First Number : {a} Second Number {b}")
