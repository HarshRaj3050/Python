# write a python program to get the fibonacci series between 0 to 55.

def fibonacci(limit):
    prev = 0
    current = 1
    list_fibonacci = []
    while(prev <= limit):
        list_fibonacci.append(prev)
        prevprev = prev
        prev = current
        current = prev + prevprev
    return list_fibonacci

limit = 55
fibo = fibonacci(limit)
print(fibo)
