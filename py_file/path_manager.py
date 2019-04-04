#  Project: py_util_pkg
#  Module: py_util_pkg
#  Last Modified: 4/1/19, 3:57 PM
#  Modified By: LaurentStanevich
#
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
#
# ######################################################################################

"""Public Docstring."""


import os

from pathlib import PurePosixPath, PureWindowsPath


def is_posix_path(my_path: str) -> bool:
    """VERSION 1: Type annotation only."""
    return "/" in str(my_path)


def is_posix_path2(my_path):
    """VERSION 2: Return whether or not a given path is Posix-based.

    :type my_path: str
    """
    return "/" in str(my_path)


def is_posix_path3(my_path):
    """VERSION 3: Return whether or not a given path is Posix-based."""
    return "/" in str(my_path)


x = is_posix_path2("//testpath")


class ObjPath:
    """Stub Docstring."""

    def __init__(self, my_path: str, is_posix: bool = False):
        """Initialize 'ObjPath' class."""
        self._isPosix = is_posix
        self._parts = None
        self.path = my_path

    @property
    def is_posix(self) -> bool:
        """GETTER: objPath.is_posix"""
        return self._isPosix

    @property
    def path(self) -> str:
        """GETTER: objPath.path"""
        if self.is_posix:
            # logMain.DEBUG("OS: Posix")
            return str(PurePosixPath(*self._parts))
        else:
            # logMain.DEBUG("OS: Windows")
            print(self.is_posix)
            return str(PureWindowsPath(*self._parts))

    @path.setter
    def path(self, new_path: str):
        """SETTER: objPath.path"""
        if is_posix_path(new_path):
            self._parts = PurePosixPath(new_path).parts
        else:
            self._parts = PureWindowsPath(new_path).parts

        # logMain.DEBUG(("New Path Assigned: " + new_path), padBefore=1)
        # logMain.indent_raise()
        # for p in self._parts:
        #     logMain.DEBUG(p)
        # logMain.indent_lower()


# noinspection PyTypeChecker
class ObjLoc:
    """Stub Docstring."""

    def __init__(self, my_root, my_path):
        """Stub Docstring.

        :type my_root: str
        :type my_path: str
        """
        self._isPosix = is_posix_path(my_root)
        if self.is_posix:
            self._root = PurePosixPath(my_root)
        else:
            self._root = PureWindowsPath(my_root)
        self._relpath = ObjPath(my_path, self.is_posix)
        pass

    @property
    def is_posix(self):
        """Stub Docstring."""
        return self._isPosix

    @property
    def root(self):
        """Stub Docstring."""
        return self._root

    @root.setter
    def root(self, new_root):
        self._root = new_root

    @property
    def rel_path(self):
        """Stub Docstring."""
        return self._relpath.path

    @rel_path.setter
    def rel_path(self, new_rel_path):
        self._relpath.path = new_rel_path

    @property
    def path(self):
        """Stub Docstring."""
        return os.path.join(self.root, self.rel_path)


if __name__ == "__main__":
    pass
