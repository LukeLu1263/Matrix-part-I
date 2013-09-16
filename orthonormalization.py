from orthogonalization import orthogonalize, aug_orthogonalize
from vec import Vec
from matutil import coldict2mat, mat2rowdict
from math import sqrt

def normalize(v):
    '''
    Input: A Vector v will be normalized
    Output: A Vector v be normalized
    '''
    return v/sqrt(v*v)

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    return [normalize(v) for v in orthogonalize(L)]

def djust(v, multipliers):
    '''
    input: a Vec with domain {0, 1, 2, . . . , n − 1} and an n-element list multipliers of scalars
    output: a Vec w with the same domain as v such that w[i] = multipliers[i]*v[i]
    '''
    return Vec(v.D, {i:multipliers[i]*v[i] for i in v.D})

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Qlist = list()
    Rlist = list()
    normlist = list()
    vstarlist, sigma_vecs = aug_orthogonalize(L)

    for vstar,sigma_vec in zip(vstarlist,sigma_vecs):
        q = normalize(vstar)
        normlist.append(sqrt(vstar*vstar))
        Qlist.append(q)
        Rlist.append(sigma_vec)

    for r in range(len(Rlist)):
        for k in Rlist[r].D:
            Rlist[r][k] = normlist[k] * Rlist[r][k]
    return (Qlist, Rlist)

