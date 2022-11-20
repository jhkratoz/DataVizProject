from setuptools import setup, find_packages
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='CSE6242_SPRING_TEAM85',
    version='0.1.0',
    packages=find_packages(include=['CSE6242_APP', 'CSE6242_APP.*']),
    entry_points={
        'console_scripts': ['my-command=CSE6242_APP.main:main']
    },
    install_requires=[
        required
    ]
)