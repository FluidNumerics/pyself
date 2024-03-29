#!/usr/bin/env python

import self.lagrange as lagrange
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))


interp = lagrange.interp()
interp.load(f'{path}/data/2d/solution.h5')
attr=dir(interp)

print("============================")
print("lagrangeFromFile\n")
print("============================")
print(f"Lagrange Object : \n {interp} \n")
print(f"Lagrange Object Attributes: \n {attr} \n")
print(f"Lagrange computational coordinates : \n {interp.controlPoints[:]} \n")
print("============================")
