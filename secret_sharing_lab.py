# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from vec import Vec



## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    while a0*u!=s or b0*u!=t:
        u = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    return u



## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: 0})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: one, 5: 0})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: 0})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: one, 3: 0, 4: 0, 5: 0})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: 0, 3: one, 4: 0, 5: 0})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: one, 5: one})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: 0, 5: one})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: 0, 5: 0})



## You can also use these procedure to generate a set of secret a1b1 through a4b4, but it could spend much more time.
#  Just uncomment the below line's quotation marks!
"""
from itertools import combinations
from independence import is_independent
secret_a1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_b1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_a2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_b2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_a3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_b3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_a4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
secret_b4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
vecs = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
while not all(is_independent(list(sum(x,()))) for x in combinations(vecs,3)):
    secret_a1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_b1 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_a2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_b2 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_a3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_b3 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_a4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    secret_b4 = list2vec([randGF2(), randGF2(), randGF2(), randGF2(), randGF2(), randGF2()])
    vecs = [(secret_a0, secret_b0),(secret_a1,secret_b1),(secret_a2,secret_b2),(secret_a3,secret_b3),(secret_a4,secret_b4)]
"""
