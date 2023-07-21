#!/usr/bin/env python

import self.geometry as geometry
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))


geom = geometry.semquad()
geom.load(f'{path}/data/2d/solution.h5')
attr=dir(geom)

print("============================")
print("geometryFromFile\n")
print("============================")
print(f"Geometry Object : \n {geom} \n")
print(f"Geometry Object Attributes : \n {attr} \n")
print(f"Geometry physical coordinates : \n {geom.x} \n")
print("============================")
