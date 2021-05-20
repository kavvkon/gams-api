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

gamsxcc_module = Extension('_gamsxcc',
                           extra_compile_args=extra_args,
                           extra_link_args=extra_link_args,
                           sources=['gamsxcc/C/gamsxcc_wrap.c', 'gamsxcc/C/gamsxcc.c', 'gamsxcc/C/gclgms.c', 'gamsxcc/C/gcmt.c'],
                           define_macros=[('PYPREFIXGAMSX', None), ('_CRT_SECURE_NO_WARNINGS', None)],
                           include_dirs=['_gamsxcc/C']
                        )

setup (name = 'gamsxcc',
       description='Python library to access GAMS Execution Object',
       version = '1.33.20.post1',
       ext_modules = [gamsxcc_module],
       packages=find_packages(),
       include_package_data=True,
       author='GAMS Development Corp.',
       license='MIT',
       maintainer='kavvkon',
       maintainer_email='kavvkon@gmail.com',
       url='https://github.com/kavvkon/gams-api'
       )
