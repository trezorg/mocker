#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import re

version = re.search('__version__ = "([^"]+)"',
                    open("mocker.py").read()).group(1)

setup(
    name="mocker",
    version=version,
    description="Graceful platform for test doubles in Python (mocks, stubs, fakes, and dummies).",
    author="Gustavo Niemeyer",
    author_email="gustavo@niemeyer.net",
    license="BSD",
    url="http://labix.org/mocker",
    download_url="https://launchpad.net/mocker/+download",
    py_modules=["mocker", "py3"],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_data = {'mocker': ['LICENSE', 'README.md5', 'RELEASE', 'NEWS']}
)
