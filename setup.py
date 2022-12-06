#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['numpy>=1.23', 'matplotlib>=3.5']


setup(
    author="Katherine Wuestney",
    author_email='katherineann983@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Package which implements the chaos game and a number of different historical random number generators.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['chaosgame', 'chaos game', 'iterated function system', 'barnsley fern']
    name='chaosgame',
    packages=find_packages(include=['chaosgame.py']),
    url='https://github.com/katherine983/chaosgame',
    version='0.1.0',
    zip_safe=False,
)
