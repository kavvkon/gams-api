# -*- coding: utf-8 -*-
from setuptools import setup, Extension, find_packages
import codecs
import sys
import os
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


is_64bits = sys.maxsize > 2**32
if not is_64bits:
    extra_args = ["-m32"]
else:
    extra_args = ["-m64"]
extra_link_args = extra_args

morelibs = os.getenv("MORELIBS")
if morelibs is not None:
    extra_link_args.append(morelibs)

gdxcc_module = Extension('_gdxcc',
                           extra_compile_args=extra_args,
                           extra_link_args=extra_link_args,
                           sources=['gdxcc/C/gdxcc_wrap.c', 'gdxcc/C/gdxcc.c', 'gdxcc/C/gclgms.c', 'gdxcc/C/gcmt.c'],
                           define_macros=[('PYPREFIXGDX', None), ('_CRT_SECURE_NO_WARNINGS', None)],
                           include_dirs=['gdxcc/C']
                        )

setup (name = 'gdxcc',
       description='Python library to access and modify gdx files',
       version = '8.33.2.post1',
       ext_modules = [gdxcc_module],
       packages=find_packages(),
       include_package_data=True,
       author='GAMS Development Corp.',
       license="MIT",
       maintainer='kavvkon',
       maintainer_email='kavvkon@gmail.com',
       url='https://github.com/kavvkon/gams-api'
       )
