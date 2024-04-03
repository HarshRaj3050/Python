# Python Program to Print n term of Fibonacci Series (Iterative approach).

def fibonacci(limit):
    prev = 0
    current = 1
    fibonacci_list = []
    while(prev <= limit):
        fibonacci_list.append(prev)
        prevprev = prev
        prev = current
        current = prev + prevprev
    return fibonacci_list

limit = 55
fibo = fibonacci(limit)
print("All the fibonacci value of '0' to '55'")
print(fibo)