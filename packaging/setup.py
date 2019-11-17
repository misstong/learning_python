from setuptools import setup
import setuptools

with open('README.md','r') as f:
    long_description = f.read()

setup(
    name = 'mypackage',
    long_description = long_description,
    packages = setuptools.find_packages()
)