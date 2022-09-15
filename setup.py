from setuptools import setup

setup(
    name='self',
    version='0.0.0',
    description='A python package for interfacing with the Spectral Element Library in Fortran (https://github.com/fluidnumerics/SELF)',
    url='https://github.com/fluidnumerics/selfpy',
    author='Dr. Joe Schoonover',
    author_email='joe@fluidnumerics.com',
    license='Researcher Software License',
    packages=['self'],
    install_requires=['h5py>=3.7.0'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: Researcher Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'
    ],
)
