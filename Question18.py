def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example: rabbit pairs after 6 months
print(fibonacci(6))  
