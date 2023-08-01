#!/usr/bin/env python
#


# Other SELF modules
import self.geometry as geometry

class model:
    def __init__(self):
        self.solution = None
        self.solutionGradient = None
        self.velocity = None
        self.compVelocity = None
        self.flux = None
        self.source = None
        self.fluxDivergence = None
        self.dSdt = None
        self.workSol = None
        self.prevSol = None
        self.mesh = None
        self.geom = geometry.semquad()

    def load(self, hdf5File):
        """Loads in 2-D model from SELF model output"""
        import h5py
        import dask.array as da

        self.geom.load(hdf5File)

        f = h5py.File(hdf5File, 'r')
        if 'state' in list(f.keys()):

            d = f['state/interior/solution'] 
            nvar = d.shape[1]
            N = d.shape[2]
            self.solution = da.from_array(d, chunks=(self.geom.daskChunkSize,nvar,N,N))

            d = f['state/interior/solutionGradient'] 
            self.solutionGradient = da.from_array(d, chunks=(self.geom.daskChunkSize,nvar,N,N,2))

            #d = f['state/interior/flux'] 
            #self.flux = da.from_array(d, chunks=(self.geom.daskChunkSize,nvar,N,N,2))

            #d = f['state/interior/fluxDivergence'] 
            #self.fluxDivergence = da.from_array(d, chunks=(self.geom.daskChunkSize,nvar,N,N))

        else:
            print(f"Error: /state group not found in {hdf5File}.")
            return 1
        
        if "plot" in list(f.keys()):
            d = f["plot/interior/solution"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.vis_solution = da.from_array(
                d, chunks=(self.geom.daskChunkSize, nvar, N, N)
            )

            d = f["plot/interior/x"]
            nvar = d.shape[1]
            N = d.shape[2]
            self.vis_x = da.from_array(d, chunks=(self.geom.daskChunkSize, nvar, N, N, 2))

        else:
            print(f"Warning: /plot group not found in {hdf5File}.")


        return 0 

       
