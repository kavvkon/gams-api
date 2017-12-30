GAMS Python API
===============

This repository hosts various GAMS' Python libraries which are used to access and modify the .gdx data files, and execute GAMS within Python. The main purpose is to compile them, package them and distribute them via Pypi so that it can be installable via pip and used as a dependecy in other packages.

Background
----------
This module is distributed for free by 'GAMS Development Corp' in http://gams.com/download along with GAMS. According to the license agreement, its use does not require the presence of a GAMS license file. Moreover it can be modified and redistributed for free.

However there is no easy way to install it without installing the whole gams suite and running the setup.py file in the corresponding directory and compiling the C extensions.


What is included
----------------
As a first step the directories ``gdxcc``, ``optcc`` and ``gamsxcc`` collect the python source files along with the necessary C extensions from GAMS version 24.9.2.
GAMS includes also the compiled C extensions (.so) but they are dependent on the platform and the python version and not include here.
The setup.py file has been modified to use the setuptools package which allows the distribution of binary wheels (bdist) for different python versions and platforms.
The source (sdist) is uploaded in Pypi and should work with all platforms and python versions.

Install
-------
GDX API (GAMS Data Exchange Object) : ``pip install gdxcc``

GAMSx API (GAMS Execution Object):  ``pip install gamsxcc``

OPT API (GAMS Option Object): ``pip install optcc``