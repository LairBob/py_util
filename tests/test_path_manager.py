#  Copyright (c) 2019. Laurent R.O. Stanevich
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
#  documentation files (the "Software"), to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions
#  of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
#  BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Docstring Stub."""

# noinspection PyUnresolvedReferences
import pytest

# import logging

import path_manager as pm


def test_base_features():
    """Docstring Stub."""
    tmp_loc_base = "Dev\\TestLoc\\Test"
    tmp_path_base = pm.ObjPath(tmp_loc_base)
    print("Output Path: " + tmp_path_base.path)

    tmp_loc_base = "Dev/TestLoc/Test"
    tmp_path_base = pm.ObjPath(tmp_loc_base)
    print("Output Path: " + tmp_path_base.path)


def test_path(str_root, str_loc):
    """
    Tests various flavors of base string.

    Arguments
    ---------
    str_root: string
    Root path for testing
    str_loc: string
    Relative path for testing
    """
    my_loc = pm.ObjLoc(str_root, str_loc)
    print("Base Path: " + str(my_loc.root))
    print("Location: " + my_loc.path)


if __name__ == "__main__":
    test_base_features()

    tmpLoc = "Dev\\TestLoc"
    test_path(
        "C:\\Users\\lstanevich\\Dropbox (Fluency Media)\\Fluency - Beaumont Content\\Beaumont.org Content Migration",
        tmpLoc,
    )
    test_path(
        "/Users/lstanevich/Dropbox (Fluency Media)/Fluency - Beaumont Content/Beaumont.org Content Migration",
        tmpLoc,
    )
    # test_path(str(PurePath.cwd()), tmpLoc)
