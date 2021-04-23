GAMS Python API
===============

.. image:: https://github.com/kavvkon/gams-api/actions/workflows/build_wheels.yml/badge.svg
    :target: https://github.com/kavvkon/gams-api/actions/workflows/build_wheels.yml

This repository hosts various GAMS' Python libraries which are used to access and modify the .gdx data files, and execute GAMS within Python. The main purpose is to compile them, package them and distribute them via PyPI so that it can be installable via pip and used as a dependecy in other packages. Detailed documentation of how to use these libraries can be found in the `GAMS API documentation section. <https://www.gams.com/latest/docs/API_MAIN.html#GAMS_LLAPIS>`_

**Update**: Python 3.9 wheels are included for all platforms. All builds have been moved to Github actions as it allows easier cross-platform maintenance.

Background
----------
This module is distributed for free by 'GAMS Development Corp' in the official `website <http://gams.com/download>`_ along with GAMS software. According to the license agreement, its use does not require the presence of a GAMS license file. Moreover it can be modified and redistributed for free.

However there is no easy way to install it without installing the whole gams suite and running the setup.py file in the corresponding directory and compiling the C extensions.


What is included
----------------
As a first step the directories ``gdxcc``, ``optcc`` and ``gamsxcc`` collect the python source files along with the necessary C extensions from GAMS version 24.9.2.
GAMS includes also the compiled C extensions (.so) but they are dependent on the platform and the python version and not include here.
The setup.py file has been modified to use the setuptools package which allows the distribution of binary wheels (bdist) for different python versions and platforms.
The source (sdist) is uploaded in Pypi and should work with all platforms and python versions.

Github actions are used to compile the packages and create the 'wheels' for various platforms and python versions.
The package `cibuildwheel <https://github.com/joerick/cibuildwheel>`_ is used to automate this task. All wheels are uploaded to PyPI.
Currently the following platforms are built:

* *Python versions*: Cpython2.7, 3.5, 3.6, 3.7, 3.8, 3.9; PyPy 2.7 v7.3.3, PyPy 3.6 v7.3.3
* *Platforms*: macOS Intel, macOS Apple Silicon, Windows 64bit, Windows 32bit, manylinux x86_64,	manylinux i686, manylinux aarch64, manylinux ppc64le, manylinux s390x

NB: Not all combinations are applicable, for more info check cibuildwheel for more info

Install
-------
GDX API (GAMS Data Exchange Object) : ``pip install gdxcc``

GAMSx API (GAMS Execution Object):  ``pip install gamsxcc``

OPT API (GAMS Option Object): ``pip install optcc``

Versioning
----------
Versioning is quite complicated as the libraries have their own version probably based on API changes. However, every GAMS release may include modifications even if API version number remains the same.
The following versioning scheme is selected:

``API_version.GAMS_major.GAMS_minor``

Currently, the latest versions built are:

* `gdxcc`: 7.28.20
* `optcc`: 4.28.20
* `gamsxcc`: 1.28.20