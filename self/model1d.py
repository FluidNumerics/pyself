#!/usr/bin/env python
#


# Other SELF modules
import self.geometry as geometry


class model:
    def __init__(self):
        self.solution = None # Dask data
        self.pvdata = None # Pyvista data
        self.varnames = None
        self.geom = geometry.semline()

    def load(self, hdf5File):
        """Loads in 1-D model from SELF model output"""
        import h5py
        import dask.array as da

        self.geom.load(hdf5File)
        
        f = h5py.File(hdf5File, "r")
        self.varnames = []

        if "controlgrid" in list(f.keys()):
            d = f["controlgrid/solution/interior"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.solution = da.from_array(d, chunks=(self.geom.daskChunkSize, nvar, N))

            d = f['controlgrid/solution/metadata/name']
            for k in d.keys():
                self.varnames.append(d[k][0].decode())

        else:
            print(f"Error: /controlgrid group not found in {hdf5File}.")
            return 1

        if "targetgrid" in list(f.keys()):
            d = f["targetgrid/solution/interior"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.vis_solution = da.from_array(
                d, chunks=(self.geom.daskChunkSize, nvar, N)
            )

        else:
            print(f"Warning: /targetgrid group not found in {hdf5File}.")

        return 0
