#!/usr/bin/env python
#

import self.lagrange as lagrange


class semquad:
    def __init__(self):

        self.interp = lagrange.interp()
        self.nElem = 0 # Number of elements
        self.x = None # physical coordinates at quadrature points
        self.dxds = None # Covariant basis vectors at quadrature points
        self.dsdx = None # Contravariant basis vectors at quadrature points
        self.J = None # Jacobian at quadrature points
        self.daskChunkSize=1000 # number of elements per dask chunk

    def load(self, hdf5File):
        """Loads in interpolant and geometry data from SELF model output"""
        import h5py
        import dask.array as da

        self.interp.load(hdf5File)

        f = h5py.File(hdf5File, 'r')
        if 'mesh' in list(f.keys()):

            d = f['mesh/interior/x'] 
            self.nElem = d.shape[0]
            nvar = d.shape[1]
            N = d.shape[2]
            self.x = da.from_array(d, chunks=(self.daskChunkSize,nvar,N,N,2))

        else:
            print(f"Error: /mesh group not found in {hdf5File}.")
            return 1

        return 0


