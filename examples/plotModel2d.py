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
print(f"Model2D Object : \n {model} \n")
print(f"Model2D Object Attributes : \n {attr} \n")
print(f"Model2D Solution : \n {model.solution} \n")
print(f"Model2D Solution (Vis): \n {model.vis_solution} \n")
print(f"Model2D Geometry (Vis) : \n {model.vis_x} \n")
print("============================")

(nelem, nvar, nx, ny) = model.vis_solution.shape
print(f"{nelem}, {nvar}, {nx}, {ny}")
n_points = nelem*nx*ny
n_faces = nelem*(nx-1)*(ny-1)


# Need to use the plot mesh to create a flat list of (x,y,z=0) points
# number of points = (M+1)*(M+1)*nelem
# dimension ordering (i,j,iel)
# Get the x-y points in flattened array for building unstructured data
np_points = np.zeros((n_points,3))
np_points[:,0] = model.vis_x[:,:,:,:,0].flatten()
np_points[:,1] = model.vis_x[:,:,:,:,1].flatten()

# Need to construct the faces from here..
# Number of faces = M*M*nelem
faces = np.zeros((n_faces,5),dtype=np.int64)
fid = 0
for iel in range(0,nelem):
    for j in range(0,ny-1):
        for i in range(0,nx-1):
            # lower left corner
            n0 = i + nx*( j + ny*iel )
            # lower right corner
            n1 = i+1 + nx*( j + ny*iel )

            # upper right corner
            n2 = i+1 + nx*( j+1 + ny*iel )

            # upper left corner
            n3 = i + nx*( j+1 + ny*iel )

            faces[fid,:] = [4, n0, n1, n2, n3]
            fid += 1
            
poly_data = pv.PolyData(np_points, faces)
# set the density to the vis solution (example data is from compressible navier stokes.)
poly_data.point_data["values"] = model.vis_solution[:,2,:,:].flatten()
pl = pv.Plotter()
pl.add_mesh(poly_data)
pl.camera_position = 'xy'
pl.show()
