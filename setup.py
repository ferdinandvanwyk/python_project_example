#!/usr/bin/env python
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mean",
    version = "0.0.4",
    author = "Ferdinand van Wyk",
    description = ("An example of how to set up pytest."),
    license = "GNU",
    keywords = "example pytest tutorial",
    packages=['mean', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
