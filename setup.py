import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version('0.0.2.1', __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()


setup(
    name='silverpop',
    version=version,
    description='Silverpop API wrapper.',
    author='Thomas Welfley',
    author_email='thomas@yola.com',
    url='https://github.com/yola/silverpop',
    packages= ['silverpop',],
    install_requires=['elementtree==1.2.7-20070827-preview'],
    license='GPL',
)
