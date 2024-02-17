from os.path import join, dirname
from setuptools import setup, find_packages


setup(
    name='lesson_2',
    version='0.2',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
