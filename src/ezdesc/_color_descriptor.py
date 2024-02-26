"""ColorDescriptor provides a descriptor class for QColor."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any, Self

from PySide6.QtGui import QColor

from ezdesc import TypedDescriptor
from ezdesc._int_field import IntField


class ColorDescriptor(TypedDescriptor):
  """ColorDescriptor provides a descriptor class for QColor."""

  red = IntField(144)
  green = IntField(255)
  blue = IntField(0)

  def __init__(self, *args) -> None:
    """Initializes the descriptor. """
    TypedDescriptor.__init__(self, QColor, *args)

  #
  def __get__(self, instance: Any, owner: type) -> QColor | Self:
    """Returns the value of the descriptor."""
    if instance is None:
      return self
    
    red = IntField.__get__(self.red, instance, owner)
    green = IntField.__get__(self.green, instance, owner)
    blue = IntField.__get__(self.blue, instance, owner)
    return QColor(red, green, blue)
