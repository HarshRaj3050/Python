# Python Program to Print n term of Fibonacci Series (Recursive approach).

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

num = int(input("Enter the number : "))
fibo = fibonacci(num)
print(f"Fibonacci of {num} is : {fibo}")