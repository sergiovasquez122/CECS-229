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
    if b == 0:
        return a
    else: 
        return gcd(b, a % b)
