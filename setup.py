from setuptools import find_packages
from setuptools import setup
from glob import glob

setup(
      packages=find_packages('src'),
      package_dir={'': 'src'},
)
