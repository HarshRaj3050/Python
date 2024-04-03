# WAP to calculate Simple Interest.

p = float(input("Enter the principal: "))
r = float(input("Enter the rate: "))
t = float(input("Enter the time: "))
si = (p * r * t) / 100
print(f"The Simple interest is {si:.2f}")