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
        if 'metadata' in list(f.keys()):
            d = f['metadata/vars']
            for k in d.keys():
                self.varnames.append(d[k][0].decode())

        if "state" in list(f.keys()):
            d = f["state/solution/interior"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.solution = da.from_array(d, chunks=(self.geom.daskChunkSize, nvar, N))

        else:
            print(f"Error: /state group not found in {hdf5File}.")
            return 1

        if "plot" in list(f.keys()):
            d = f["plot/state/solution/interior"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.vis_solution = da.from_array(
                d, chunks=(self.geom.daskChunkSize, nvar, N)
            )

        else:
            print(f"Warning: /plot group not found in {hdf5File}.")

        return 0
