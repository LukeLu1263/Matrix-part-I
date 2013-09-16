# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [ L[i] for i in range(len(L)) if L[i] % num != 0 ]



## Problem 2
def myLists(L): return [ list(range(1,L[x]+1)) for x in range(len(L)) ]



## Problem 3
def myFunctionComposition(f, g): return { k: g[v] for (k,v) in f.items() }


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1+0.001j
complex_addition_d = 0.001+9j

import pdb; pdb.set_trace()  # XXX BREAKPOINT


## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for i in range(len(L)):
        sum += L[i]
    return sum



## Problem 7
def myProduct(L):
    product = 1
    for i in range(len(L)):
        product *= L[i]
    return product


## Problem 8
def myMin(L):
    minimum = 9**10
    for i in range(len(L)):
        if minimum > L[i]:
            minimum = L[i]
    return minimum



## Problem 9
def myConcat(L):
    strings = ''
    for i in range(len(L)):
        strings += L[i]
    return strings



## Problem 10
def myUnion(L):
    union = set()
    for i in range(len(L)):
        union |= L[i]
    return union

