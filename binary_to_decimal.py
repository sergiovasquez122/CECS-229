'''
This program converts a binary string to decimal
@author Sergio Vasquez
@version 08/13/2020
@file binary_decimal.py
'''
def binary_to_decimal(s):
    '''
    s: a string that represents a unsigned-integer in binary notation
    returns a integer that is the base 10 decimal of the string
    '''
    value = 0
    for s_i in s:
        value = value * 2 + (0 if s_i == '0' else 1)
    return value
