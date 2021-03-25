#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import require, VersionConflict
from setuptools import setup

from setuptools_rust import Binding, RustExtension

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

import subprocess 
toolchains = subprocess.check_output(["rustup", "toolchain", "list"]).decode('utf-8').split("\n")
import os
print("USING", os.environ.get('RUSTUP_TOOLCHAIN',''))


if __name__ == "__main__":
    setup(
        rust_extensions=[RustExtension("mbf_nested_intervals.mbf_nested_intervals", 
                                       binding=Binding.PyO3, debug=False)],
    )
