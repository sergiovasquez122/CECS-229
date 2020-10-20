'''
This program uses the sieve of Eratosthenes
to find all primes less than 10,000
@author Sergio Vasquez
@version 10/19/2020
@file sieve_of_eratosthenes.py
'''
from math import *

def sieve(n):
    '''
    n: An integer that is greater than or equal
    to 2
    return a list of all primes that are 
less than or equal to n
    '''
    marked = [True for i in range(n + 1)]

    for i in range(2, int(sqrt(n)) + 1):
        if marked[i]:
            for j in range(2 * i, n + 1,i):
                marked[j] = False

    marked[0] = False
    marked[1] = False
    result = []
    for idx, value in enumerate(marked):
        if value == True:
            result.append(idx)
    return result

print(sieve(10000))
