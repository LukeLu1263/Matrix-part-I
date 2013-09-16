## week4 slides 10 Perspective_rectification
from image_mat_util import *

from mat import Mat
from vec import Vec
from matutil import rowdict2mat, mat2coldict, coldict2mat

from solver import solve

## Task 1
def move2board(v):
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, {d: v[d]/v['y3'] for d in v.D})

## Task 2
def make_equations(x1, x2, w1, w2):
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1, ('y3','x2'):w1*x2, ('y3','x3'):w1, ('y1','x1'):-x1, ('y1','x2'):-x2, ('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):w2*x1, ('y3','x2'):w2*x2, ('y3','x3'):w2, ('y2','x1'):-x1, ('y2','x2'):-x2, ('y2','x3'):-1})
    return [u, v]


def get_H():
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    w = Vec(domain, {('y1','x1'):1})
    l1 = make_equations(358, 36, 0, 0)
    l2 = make_equations(329, 597,0, 1)
    l3 = make_equations(592, 157,1, 0)
    l4 = make_equations(580, 483,1, 1)
    rowdict = { 0:l1[0],
                1:l1[1],
                2:l2[0],
                3:l2[1],
                4:l3[0],
                5:l3[1],
                6:l4[0],
                7:l4[1],
                8:w    }
    L = rowdict2mat(rowdict)
    b = Vec(set(range(9)), {8:1})
    h = solve(L, b)
    return Mat(({a for a in {'y1','y2','y3'}}, {b for b in {'x1','x2','x3'}}), {(d[0],d[1]):h[d] for d in h.D})


## Task 3
H = get_H()


## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane
          of the line through the origin and q).
    '''
    col_Y = mat2coldict(Y)
    return coldict2mat({d:move2board(col_Y[d]) for d in col_Y})


## Sample
# (X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
# Y_pts = H * X_pts
# Y_board = mat_move2board(Y_pts)
# mat2display(Y_board, colors, ('y1','y2','y3'), scale=100, xmin=None, ymin=None)
