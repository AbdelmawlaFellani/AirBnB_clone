#!/usr/bin/python3
"""Unittest test_console module"""

import unittest
from unittest.mock import patch
from io import StringIO
import console
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    """TestHBNBCommand class"""
