def print_1toN(n):
    if n < 1:
        print("Please provide a positive integer greater than 0.")
        return
    if n == 1:
        print(1)
    else:
        print_1toN(n - 1)
        print(n)

print_1toN(10)
