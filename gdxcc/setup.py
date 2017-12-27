from setuptools import setup, Extension, find_packages
import codecs
import sys
import os
LICENSE = 'THE GAMS FREE APIS ARE PROVIDED "AS IS" AND GAMS DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL GAMS BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THE GAMS FREE APIS.'
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
                           sources=['gdxcc/C/gdxcc_wrap.c', 'gdxcc/C/gdxcc.c'],
                           define_macros=[('PYPREFIXGDX', None), ('_CRT_SECURE_NO_WARNINGS', None)],
                           include_dirs=['gdxcc/C']
                        )

setup (name = 'gdxcc',
       description='Python library to access and modify gdx files',
       version = '7-2492',
       ext_modules = [gdxcc_module],
       packages=find_packages(),
       include_package_data=True,
       author='GAMS Development Corp.',
       license=LICENSE,
       maintainer='kavvkon',
       maintainer_email='kavvkon@gmail.com'
       )
