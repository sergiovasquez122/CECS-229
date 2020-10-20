'''
This program asks users for two primes numbers
then generates an n and e for the RSA cryptosystem
@author Sergio Vasquez
@version 10/19/2020
@file RSA.py
'''
def gcd(a, b):
    '''
    a: a non-negative integer
    b: a non-negative integer less than or equal to a
    returns an integer that is the greater common divisor of a and b'''
    return a if b == 0 else gcd(b, b % a)

def relative_prime_number(n):
    '''
    n: a positive integer
    returns an integer that is relatively prime to this number
    return None if such a number does not exist'''
    for i in range(1, n):
        if gcd(i, n) == 1:
            return i
    return None

p = input("Enter valid prime p: ")
q = input("Enter valid prime q: ")
p = int(p)
q = int(q)
n = p * q
e = relative_prime_number((p - 1) * (q - 1))

if type(e) == int:
    print("n:", p * q)
    print("e:", e)
