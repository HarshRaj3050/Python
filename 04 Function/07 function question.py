# Python Program to Print n term of Fibonacci Series (Iterative approach).

def fibonacci(num):
    prev = 0
    current = 1
    for i in range(1, num):
        prevprev = prev
        prev = current
        current = prev + prevprev
    return current

num = int(input("Enter the number "))
fibo = fibonacci(num)
print(f"Fibonacci of {num} is : {fibo}")