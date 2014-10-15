# !/usr/bin/python
# vim: set fileencoding=utf8 :
#
__author__ = 'keping'

from setuptools import setup, find_packages


setup(
    name='minipig',
    version='0.0.1',
    author='Cping Ju',
    author_email='zkp1985@gamil.com',
    url='https://github.com/spidermachine/minipig',
    description='A mini async/sync message process framework with multiple threads.',
    packages=('minipig', ),
    long_description="mini pig",
    keywords='minipig',
    zip_safe=False,
    include_package_data=True,
)