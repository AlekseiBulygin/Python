"""
Triangulation between two polygons (convex or concave hull)
Use Triangle - python wrapper around Jonathan Richard Shewchuk’s
two-dimensional quality mesh generator.
"""
import matplotlib.pyplot as plt
import triangle as tr

polygon = [[0, 0], [0, 4], [2, 4], [2, 5], [3, 5], [3, 8], [6, 4], [6, 0]]
offset_polygon = [[2, 1], [2, 3], [4, 3], [4, 1]]

A = {'vertices': polygon + offset_polygon,
     'segments': [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 0], [8, 9], [9, 10], [10, 11], [11, 8]],
     'holes': [[3, 2]]}               # holes - point(s) coord(x, y) inside hole(must be circled in segments)
B = tr.triangulate(A, 'pa1')          # 'p' - create mesh with holes,
print(B['triangles'].tolist())        # 'a1' - create new point for more small mesh


tr.compare(plt, A, B)
plt.show()
