from mat import *
from vec import *
from cancer_data import *

## Ungraded Task:Use read_training_data to read the data in the file train.data into the variables A, b.
A,b = read_training_data("./train.data")

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    v = Vec(u.D, {})
    for d in u.D:
        if u[d] >= 0:
            v[d] = 1
        else:
            v[d] = -1
    return v

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w
    '''
    length = len(b.D)
    dot_product = signum(A*w)*b
    return (length - dot_product) / (2*length)

## Task 3 ##
# Hint: when you hear "sum of squares of vector's elements" or "square of vector's norm" you should think "dot product with itself". "
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    u = A*w-b
    return (u*u)

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2*(A*w-b)*A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma*find_grad(A, b, w)

## Ungraded Task:
def gradient_descent(A, b, w, sigma, T):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
        - T: iteration times
    Output:
        - smallest value w after runing gradient descent algorithm
    '''
    smallest = Vec(w.D, {})
    for i in range(T):
        smallest = gradient_descent_step(A, b, w, sigma)
    return smallest

## Ungraded Task:
sigma1 = (1e-9)
sigma2 = (1e-9)*2
