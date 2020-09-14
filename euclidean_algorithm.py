'''
This program calculates the greatest common divsor
of two numbers
@author Sergio, Vasquez
@version 08/13/2020
@file euclidean_algorithm.py'''
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

