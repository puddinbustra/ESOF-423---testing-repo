#from setuptools import setup
from distutils.core import setup
from glob import glob
from setuptools import find_packages


setup(
      packages=find_packages('src'),
      package_dir={'': 'PsyGuideSite'},
     )
