"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys

from pyperclip import copy

from tester_class_01 import Tester01


def tester00() -> None:
  """Hello world"""
  stuff = [os, sys, 'hello world', copy]
  for item in stuff:
    print(item)


def tester01() -> None:
  """Hello world"""
  test = Tester01()


if __name__ == '__main__':
  tester01()
