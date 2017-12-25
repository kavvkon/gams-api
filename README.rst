GAMS Python API
===============

This repository hosts the Python GAMS API which is used to access and modify the .gdx data files. Its main purpose is to compile it, package it and distribute it via Pypi so that it can be installable via pip and used as a dependecy in other packages.

Background
----------
The GAMS API is distributed for free by 'GAMS Development Corp' in http://gams.com/download along with GAMS. According to the license agreement, its use does not require the presence of a GAMS license file. Moreover it can be modified and redistributed for free.

However there is no easy way to install it without installing the whole gams suite and running the setup.py file in the corresponding directory and compiling the C extensions.


What is included
----------------
As a first step the directory gdxcc collects the python source files along with the necessary C extensions `gdxcc_wrap.c` `gdxcc.c` `gdxcc.h` from GAMS version 24.9.2.
GAMS includes also the compiled C extensions (.so) but they are dependent on the platform and the python version and not include here.
The setup.py file has been modified to use the setuptools package which allows distribution of binary wheels (bdist) for different python versions and platforms.
The source (sdist) is uploaded in Pypi.

Install
-------
`pip install gdxcc`