def print_Nto1(n):
    if n < 1:
        print("Please provide a positive integer greater than 0.")
        return
    print(n)
    print_Nto1(n - 1)

print_Nto1(10)
