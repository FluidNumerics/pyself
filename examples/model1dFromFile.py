#!/usr/bin/env python

import self.model1d as model1d
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

model = model1d.model()
model.load(f'{path}/data/1d/solution.h5')
attr=dir(model)

print("============================")
print("model1DFromFile\n")
print("============================")
print(f"Model1D Object : \n {model} \n")
print(f"Model1D Object Attributes : \n {attr} \n")
print(f"Model1D Solution : \n {model.solution} \n")
print("============================")
