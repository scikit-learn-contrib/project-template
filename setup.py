from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

setup(name='scikit-learn stub',
      version='0.1.0_dev',
      description='A template for scikit-learn compatible packages',
      author='Vighnesh Birodkar',
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      author_email='vighneshbirodkar@nyu.edu',
      )
