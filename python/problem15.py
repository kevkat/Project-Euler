#!/usr/bin/python
def binomialCoefficient(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    diff = n - k
    if k > diff: # take advantage of symmetry
        k = diff
    c = 1
    for i in range(k):
        c = c * (n - i) / (i + 1)
    return c

print binomialCoefficient(40, 20)