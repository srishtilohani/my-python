# Fibonacci series of first 10 numbers

def fibonacci_series(n):
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

# Print first 10 Fibonacci numbers
fibonacci_series(10)
