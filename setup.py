#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ores
from setuptools import setup

version = ores.__version__

setup(
    name='ores-cli',
    version=version,
    packages=["ores"],
    entry_points={
        "console_scripts": ['ores = ores.__main__:main']},
    description='ORES Python API client and CLI utility',
    author='Cristian Consonni',
    author_email='cristian.consonni@unitn.it',
    url="https://github.com/CristianCantoro/ores-python"
    )
