#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup


install_description = '''
saturn fs
===========

Python library for saturn file storage
'''

setup(
    name='saturn-fs',
    version='0.0.1',
    packages=['mimas', 'mimas.fs'],
    author='chenwenquan',
    author_email='chenwenquan@le.com',
    description='Python library for saturn file storage',
)
