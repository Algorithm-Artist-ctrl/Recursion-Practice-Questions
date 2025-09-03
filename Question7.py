def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

x = int(input("Enter first number:\n"))
y = int(input("Enter second number:\n"))

print("GCD is:", gcd(x, y))
print("LCM is:", lcm(x, y))
