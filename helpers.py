def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    greatest_common_divisor, x1, y1 = gcdExtended(b % a, a)
    x = y1 - ( b // a) * x1
    y = x1
    return greatest_common_divisor, x, y
