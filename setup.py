# -*- coding: utf-8 -*-

import os
from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as readme_file:
    README = readme_file.read()

with open(os.path.join(here, 'CHANGES.txt')) as changes_file:
    CHANGES = changes_file.read()

install_requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    ]

tests_require = []

testing_extras = [
    'nose'
    ]

def main():
  setup(name='trypyramid',
        version='0.1',
        description='TryPyramid Quickstart Site',
        long_description=README + '\n\n' + CHANGES,
        classifiers=[
            "Programming Language :: Python",
            "Framework :: Pyramid",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          ],
        author='',
        author_email='',
        url='',
        keywords='web pyramid pylons',
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=install_requires,
        tests_require=tests_require,
        extras_require = {
            'testing': testing_extras,
            },
        test_suite="trypyramid",
        entry_points="""\
        [paste.app_factory]
        main = trypyramid:main
        """,
        )

if __name__ == '__main__':
    main()
