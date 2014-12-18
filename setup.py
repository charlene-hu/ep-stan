"""Compile Cython module util in file `util.pyx` into file `util.so`.

Compile with:
$ python setup.py build_ext --inplace

"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("util.pyx")
)

