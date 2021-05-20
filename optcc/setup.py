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

optcc_module = Extension('_optcc',
                           extra_compile_args=extra_args,
                           extra_link_args=extra_link_args,
                           sources=['optcc/C/optcc_wrap.c', 'optcc/C/optcc.c', 'optcc/C/gclgms.c', 'optcc/C/gcmt.c'],
                           define_macros=[('PYPREFIXOPT', None), ('_CRT_SECURE_NO_WARNINGS', None)],
                           include_dirs=['optcc/C']
                        )

setup (name = 'optcc',
       description='Python library to access GAMS Option Object',
       version = '4.33.20.post1',
       ext_modules = [optcc_module],
       packages=find_packages(),
       include_package_data=True,
       author='GAMS Development Corp.',
       license='MIT',
       maintainer='kavvkon',
       maintainer_email='kavvkon@gmail.com',
       url='https://github.com/kavvkon/gams-api'
       )
