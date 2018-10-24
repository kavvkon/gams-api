from __future__ import print_function
from gdxcc import *
import os

def test_write_gdx():
    GAMS_DIR = os.path.normpath(os.environ['GAMS_DIR'])
    print("using GAMS system directory:", GAMS_DIR)
    print(find_file('libgdxdclib64.dylib',root_path()))
    print(find_file('dxdclib.dll',root_path()))
    print(find_file('libgdxdclib64.so',root_path()))

    ## START TESTS
    gdxHandle = new_gdxHandle_tp()
    rc = gdxCreateD(gdxHandle, GAMS_DIR, GMS_SSSIZE)
    assert rc[0], rc[1]

    print("Using GDX DLL version: " + gdxGetDLLVersion(gdxHandle)[1])

    assert gdxOpenWrite(gdxHandle, "demanddata.gdx", "xp_example1")[0]
    assert gdxDataWriteStrStart(gdxHandle, "Demand", "Demand data", 1, GMS_DT_PAR, 0)

    values = doubleArray(GMS_VAL_MAX)

    values[GMS_VAL_LEVEL] = 324.0
    gdxDataWriteStr(gdxHandle, ["New-York"], values)
    values[GMS_VAL_LEVEL] = 299.0
    gdxDataWriteStr(gdxHandle, ["Chicago"], values)
    values[GMS_VAL_LEVEL] = 274.0
    gdxDataWriteStr(gdxHandle, ["Topeka"], values)

    assert gdxDataWriteDone(gdxHandle)
    print("Demand data written by xp_example1")

    assert not gdxClose(gdxHandle)
    assert gdxFree(gdxHandle)

    print("All done xp_example1")

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def root_path():
    return os.path.abspath(os.sep)