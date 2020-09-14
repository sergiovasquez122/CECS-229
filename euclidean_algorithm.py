'''
This program calculates the greatest common divsor
of two numbers
@author Sergio, Vasquez
@version 08/13/2020
@file euclidean_algorithm.py
'''
def gcd(a, b):
    '''
    a: a non-negative integer
    b: a non-negative integer less than or equal to a
    returns a integer that is the greatest common divisor of a and b
    '''
    return a if b == 0 else gcd(b, a % b)
