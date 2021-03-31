# -*- coding: utf-8 -*-
"""
REST2 package
"""
import os
from .version import __version__

REST2DIR = os.path.dirname(os.path.realpath(__file__))
TESTDATADIR = os.path.join(os.path.dirname(REST2DIR), 'tests', 'data')
