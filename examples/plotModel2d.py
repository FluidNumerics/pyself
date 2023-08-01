import numpy as np
import pyvista as pv
import self.model2d as model2d
import inspect, os.path

# Get full path to examples/
# From https://stackoverflow.com/questions/2632199/how-do-i-get-the-path-of-the-current-executed-file-in-python
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

model = model2d.model()
model.load(f'{path}/data/2d/solution.h5')
attr=dir(model)

print("============================")
print("model2DFromFile\n")
print("============================")
print(f"Model2D PyVista data : \n {model.pvdata} \n")
print("============================")

# Use the "active_scalars_name" field to set which field is plotted.
model.pvdata.point_data.active_scalars_name = "rho"

print(model.pvdata.point_data)

# Plot the field in 2-d
pl = pv.Plotter()
pl.add_mesh(model.pvdata)
pl.camera_position = 'xy'
pl.show()
