# Quick Start

## Install pyself

pySELF can be installed using pip.

```
pip install pyself==0.0.0
```

If you'd like to install a non-tagged version, from the `main` branch for example, see [Installation](./Installation.md).

## Read in SELF data from a file
Suppose that you have run a simulation with SELF using the `Model2D` class or one of its children (e.g. `LinearShallowWater2D`). The simulation has generated a set of `solution.*.h5` files. In the scenario described here, we're interested in loading in the contents of a file called `solution.example.h5` in the current working directory.

```
#!/usr/bin/env python

import self.model2d as model2d


# Initialize your model
model = model2d.model()

# Load in the model data from file
model.load('solution.example.h5')
```

## Working with model data
The model class in pyself provides many of the same attributes as the equivalent class in SELF.

* `solution` - The solution array at element interior (quadrature) points
* `solutionGradient` - The gradient of the solution at element interior (quadrature) points
* `flux` - The conservative flux vector at element interior (quadrature) points
* `fluxDivergence` - The divergence of the flux vector at element interior (quadrature) points

Each of these attributes are stored as [Dask arrays](https://docs.dask.org/en/stable/array.html). The data stored in these attributes can be accessed in the same way as you would numpy arrays.

The dimension ordering that is used for these arrays (in 2-D) is as follows: 

1. Element dimension
2. Variable dimension
3. Quadrature dimension (second computational direction)
4. Quadrature dimension (first computational direction)
5. (Optional) Physical Vector direction

For example,

```
solutionData = model.solution[iel,ivar,:,:]
```

stores the `ivar`-th solution variable within the `iel`-th element in `solutionData`.



## Working with mesh, geometry, and interpolant data
Additionally, the model class has `mesh` and `geometry` objects as attributes. In version `0.0.0` (the current version), the `mesh` object is not filled in; this means that you currently don't have access to connectivity information. The `geometry` class, on the other hand, contains the following attributes :

* `interp` - The Lagrange interpolant object that defines coordinates and operators in computational space for the geometry and model data
* `x` - The coordinates in physical space at element interior (quadrature) points

As with the `model` attributes, the `x` attribute is stored as a [Dask array](https://docs.dask.org/en/stable/array.html). To obtain the `x` and `y` positions as their own arrays, you can do something like the following,

```
# Get x and y physical coordinates for all elements and quadrature points
x = model.geom.x[:,:,:,:,0]
y = model.geom.y[:,:,:,:,0]
```
