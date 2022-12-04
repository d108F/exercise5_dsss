# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:02:00 2022

@author: daniel
"""

from distutils.core import setup
from setuptools import find_packages

setup(
      name="snowflake",
      version="0.1",
      author="Daniel Fleischhauer",
      packages=find_packages(),
      install_requires=["numpy", "turtles"]
      )