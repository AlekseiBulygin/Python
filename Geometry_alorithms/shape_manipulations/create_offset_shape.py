"""Three methods to create offset shape"""
import matplotlib.pyplot as plt
from shapely.geometry.polygon import LinearRing, LineString
import pyclipper
import shapely.geometry as shp


def plot_line(ax, ob, color):
    x, y = ob.xy
    ax.plot(x, y, color=color, alpha=0.7, linewidth=3,
            solid_capstyle='round', zorder=2)

polygon = [[3, 1], [1, 3], [1, 6], [3, 9], [6, 9], [8, 6], [8, 3], [6, 1]]


line = LineString(polygon)

poly_line_offset = line.parallel_offset(1, side="right", resolution=16, join_style=2)

##########################

# afpoly = shp.Polygon(polygon)
# noffafpoly = afpoly.buffer(-1, join_style=2)  # Inward offset
# poly_line_offset = noffafpoly.exterior
# print(poly_line_offset)

###########################

# pco = pyclipper.PyclipperOffset()
# pco.AddPath(polygon, pyclipper.JT_MITER, pyclipper.ET_CLOSEDPOLYGON)
# poly_line_offset = LinearRing(pco.Execute(-1.0)[0])

###########################

fig = plt.figure()
ax = fig.add_subplot(111)
plot_line(ax, line, "blue")
plot_line(ax, poly_line_offset, "green")
plt.show()
