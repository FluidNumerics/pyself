# SELF for Python

The [Spectral Element Library in Fortran (SELF)](https://github.com/fluidnumerics/SELF) is a Fortran library that provides Fortran classes for creating PDE solvers using Spectral Element Methods. SELF natively provides support for running on everything from local workstations to large supercomputers. It provides automatic GPU and multi-GPU acceleration when available.

SELF for Python (SELF-Py) provides a python interface for SELF. This gives you the ability to flexibly construct complete simulation workflows, without having to work in Fortran. 


## Release Notes

### Version 0.0.0
SELF-Py is currently in its infancy and provides the ability to read and write SELF model and mesh files. Current interactions with SELF is mediated through these files. This gives you the opportunity to handle pre and post-processing activities in Python. 

### Roadmap
In upcoming SELF-Py releases, we plan to give you control for setting up and running models completely from Python by hooking into the SELF API directly.


