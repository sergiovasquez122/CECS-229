from math import *

def sieve(n):
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
