## week4 video 9  Perspective_rendering

from vecutil import list2vec
from hw4 import vec2rep
from plotting import plot
from matutil import coldict2mat

a1 = list2vec([1/100, 0, 0])
a2 = list2vec([0, 1/100, 0])
a3 = list2vec([-1/2, -1/2, 1])
camera_basis = [a1, a2, a3]

pt = list2vec([1, 1, 8])
coordinate_representation = vec2rep(camera_basis, pt)
print(coordinate_representation)

print(coordinate_representation/coordinate_representation[2])

i, j = 62.5, 62.5
plot([(i,j)], 80)

def line_segment(pt1, pt2, samples=100):
    return [(i/samples)*pt1 + (1-i/samples)*pt2 for i in range(samples+1)]

corners = [list2vec([1,1,8])+list2vec(v) for v in [[0,0,0],[1,0,0],[0,1,0],[1,1,0],[0,0,1],[1,0,1],[0,1,1],[1,1,1]]]
line_segments = [line_segment(corners[i], corners[j]) for i,j in [(0,1),(2,3),(0,2),(1,3),(4,5),(6,7),(4,6),(5,7),(0,4),(1,5),(2,6),(3,7)]]
pts = sum(line_segments, [])
reps = [vec2rep(camera_basis, v) for v in pts]

def scale_down(u): return list2vec([u[0]/u[2], u[1]/u[2], 1])
in_camera_plane = [scale_down(u) for u in reps]

def pixel(u): return (u[0], u[1])
pixels = [pixel(u) for u in in_camera_plane]
# in camera plane
plot(pixels, 80, 1)
print(coldict2mat(camera_basis))


# from world coordinate to camera coordinate
import inverse
B = inverse.find_matrix_inverse(coldict2mat(camera_basis), 1)
print(B)
X = B*coldict2mat(pts)
print(X[0,0], X[1,0],X[2,0])
