from distutils.core import setup
from glob import glob

from setuptools import find_packages

setup(name='loftytests',
      version='1.0',
      description='Pain and suffering',
      author='lofty',
      packages=find_packages('tests'),
      package_dir={'': 'tests'},
      #py_modules=[splitext(basename(path))[0] for path in glob('tests/*.py')],
     )
