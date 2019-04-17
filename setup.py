#from setuptools import setup
from distutils.core import setup
from glob import glob
from setuptools import find_packages


setup(
      # packages=find_packages('PsyGuideSite'),
      # package_dir={'': 'PsyGuideSite'},
      packages=find_packages('PsyGuideSite'),
      package_dir={'': 'PsyGuideSite'},
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nirla.settings")
     )
