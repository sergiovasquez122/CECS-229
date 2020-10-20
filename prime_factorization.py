'''
This program find all of the positive divisors
of a positive integer from its prime factorization
@author Sergio Vasquez
@version 10/19/20
@file prime_factorization.py
'''

from math import *
from numpy import prod
from itertools import *

def prime_factors(n):
    '''
    n: A positive integer
    returns a list of all primes as an array
    '''
    result = []
    while n % 2 == 0:
        result.append(2)
        n /= 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(int(i))
            n /= i

    if n > 2:
        result.append(n)

    return result

def all_positive_divisors(n):
    '''
    n: a positive integer n
    returns all positive divisors as a set
    '''
    lst = prime_factors(n)
    divisors = [1] + lst
    return set([prod(x) for i in range(1, len(divisors) + 1) for x in
                combinations(divisors, i)])

