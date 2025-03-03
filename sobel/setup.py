from setuptools import setup
from Cython.Build import cythonize
import numpy 

setup(
    ext_modules = cythonize("sobel_filter.pyx"),
    include_dirs=[numpy.get_include()]  # Asegúrate de que la ruta de numpy esté incluida
)
