import os
import sys
from setuptools import setup, find_packages


def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


# Python version check.
if sys.version_info < (3, 6):
    sys.exit('BioMASS requires at least Python version 3.6')

setup(
    name='biomass',
    description='Modeling and Analysis of Signaling Systems',
    license='MIT',
    author='Hiroaki Imoto',
    author_email='himoto@protein.osaka-u.ac.jp',
    url='https://github.com/okadalabipr/biomass',
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires='>=3.6',
)