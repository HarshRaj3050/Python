# Function to generate Fibonacci series up to a given limit
def generate_fibonacci_series(limit):
    fibonacci_series = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_series.append(a)
        a, b = b, a + b
    return fibonacci_series

# Set the limit
limit = 55

# Generate and print the Fibonacci series up to the limit
fib_series = generate_fibonacci_series(limit)
print("Fibonacci series up to", limit, ":")
print(fib_series)
