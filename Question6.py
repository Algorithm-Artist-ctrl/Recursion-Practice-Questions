def gcd(p, q):
    if q == 0:
        return p
    else:
        return gcd(q, p % q)

x = int(input("Enter first number:\n"))
y = int(input("Enter second number:\n"))

print("GCD is:", gcd(x, y))
