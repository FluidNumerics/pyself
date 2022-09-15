#!/usr/bin/env python

import self.model2d as model2d
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

model = model2d.model()
model.load(f'{path}/data/solution.h5')
attr=dir(model)

print("============================")
print("model2DFromFile\n")
print("============================")
print(f"Model2D Object : \n {model} \n")
print(f"Model2D Object Attributes : \n {attr} \n")
print(f"Model2D Solution : \n {model.solution} \n")
print("============================")
