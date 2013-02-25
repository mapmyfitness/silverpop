import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='silverpop',
    version='0.0.2.1',
    description='Silverpop API wrapper.',
    author='Thomas Welfley',
    author_email='thomas@yola.com',
    url='https://github.com/yola/silverpop',
    packages= ['silverpop',],
    install_requires=['elementtree==1.2.7-20070827-preview'],
    license='GPL',
)
