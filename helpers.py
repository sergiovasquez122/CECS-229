from math import sqrt
from string import ascii_uppercase

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def gcdExtended(a, b):
    if a == 0:
        return b, 0, 1

    greatest_common_divisor, x1, y1 = gcdExtended(b % a, a)
    x = y1 - ( b // a) * x1
    y = x1
    return greatest_common_divisor, x, y

def prime_factors(n):
    while n % 2 == 0:
        print (2)
        n = n / 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            print (i)
            n = n / i

    if n > 2:
        print(n)

def isbn_10(str):
    val = 0
    for idx, digit in enumerate(str):
        val += (idx + 1) * int(digit, 10)
    return val % 11

def caesar_cipher(message, k):
    new_message = ""
    for letter in message:
        value = (ord(letter) - 65) + k
        while value < 0:
            value += len(ascii_uppercase)
        new_message += ascii_uppercase[value % len(ascii_uppercase)]
    return new_message

def affine_cipher_encrypt(message, a, k):
    new_message = ""
    for letter in message:
        new_message += ascii_uppercase[(a * ((ord(letter) - 65)) + k) % len(ascii_uppercase)]
    return new_message

def affine_cipher_decrypt(message, a, k):
    new_message = ''
    _, a_inverse, _ = gcdExtended(a, 26)
    while a_inverse < 0:
        a_inverse += 26
    for letter in message:
        value = (ord(letter) - 65) - k
        while value < 0:
            value += 26
        new_message += ascii_uppercase[((a_inverse % 26) * (value % 26)) % 26]
    return new_message
