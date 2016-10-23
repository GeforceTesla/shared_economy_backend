from __future__ import print_function, division

import os
import sys

from setuptools import find_packages


try:
    from setuptools import setup
except:
    from distutils.core import stup

with open('README') as README:
    readme = README.read()

setup(
    name='se_backend',
    version='0.1',
    description='Python packages to handle backend logic',
    long_description=readme,
    author='Luthienas',
    author_email='',
    packages=find_packages(),
    package_dir={'se_backend': 'se_backend'},
    include_package_data=True,
    keywords='se_backend'
)