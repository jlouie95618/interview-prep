# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='solutions',
    version='0.0.1',
    description='Interview Preparation',
    long_description=readme,
    author='John Louie',
    author_email='jlouie95618@gmail.com',
    url='https://jlouie95618.github.io',
    install_requires=['nose'],
    scripts=[],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

