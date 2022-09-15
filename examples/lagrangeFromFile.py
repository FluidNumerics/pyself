#!/usr/bin/env python

import self.lagrange as lagrange
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))


interp = lagrange.data()
interp.load(f'{path}/data/solution.h5')
print(interp)
print(interp.controlPoints[:])
print(interp.N)
