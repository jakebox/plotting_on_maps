# Plotting some points on a map
# By Jake Boxerman

import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Loading the map
map = gpd.read_file('./map_files/geo_export_15b8dd7a-7351-4b94-8cc1-7b2df7ef35cd.shp')

# Some fake coordinate points to use, stored in an array. Then converted to points.
add_points = np.array([[-87.70,  41.90],  
                       [-87.65, 41.95]])
points = [Point(xy) for xy in add_points]
points

# Putting the points into a GeoDataFrame
points = gpd.GeoDataFrame(points, 
                                  columns=['geometry'],
                                  crs=map.crs)
points.head(3)

# Plotting the map and the dots over it.
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
map.plot(ax = ax)
points.plot(ax = ax, marker = "o", color="red")
ax.set(xlabel = "Longitude (deg)", ylabel = "Latitude (deg)")

plt.show()