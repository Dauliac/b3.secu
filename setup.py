#!/usr/bin/env python3
# coding: utf-8
# =============================================================================
# Name     : setup.py
# Function :
# Usage    :
# Version  : 1.0.0
# vi       : set expandtab shiftwidth=4 softtabstop=4
# =============================================================================

from setuptools import setup, find_packages

long_description = """
python brutforce
"""

setup(
    name='pyforce',
    version='0.0.1',
    description='python brutforce',
    license='MIT',
    scripts=["bin/pyforce"],
    package_dir={'': 'lib'},
    author='Julien Dauliac &&',
    author_email='julien.dauliac@ynov.com',
    url='https://gitlab.dotfile.eu/dauliac/b3.secu',
    packages=find_packages('lib'),
    install_requires=[],
    long_description=long_description,
    python_requires='>=3.7',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: MIT",
        "Programming Language :: Python :: 3",
    ],
)
