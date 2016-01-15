from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

SETUP_REQUIRES = ['numpy>=1.6.1', 'scipy>=0.9', 'cython>=0.23']

setup(name='scikit-learn stub',
      version='0.1.0_dev',
      description='A template for scikit-learn compatible packages',
      author='Vighnesh Birodkar',
      packages=find_packages(),
      setup_requires=SETUP_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      author_email='vighneshbirodkar@nyu.edu',
      )
