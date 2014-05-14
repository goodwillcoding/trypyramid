#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.txt')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ''

def main():
    setup(
        name='trypyramid',
        version='0.1',
        description='TryPyramid',
        long_description=README + '\n\n' +  CHANGES,
        author='Pylons Project',
        author_email='@',
        url='https://github.com/Pylons/trypyramid',
        packages=[
            'trypyramid',
        ],
        package_dir={'trypyramid': 'trypyramid'},
        include_package_data=True,
        install_requires=[
            'sphinx'
        ],
        license="BSD",
        zip_safe=False,
        keywords='trypyramid',
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            "Programming Language :: Python :: 2",
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
        ],
        test_suite='tests',
    )

if __name__ == '__main__':
    main()
