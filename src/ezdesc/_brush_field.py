"""BrushField provides a descriptor class for QBrush."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor

from ezdesc import TypedDescriptor, ColorDescriptor

Lime = QColor(144, 255, 0)


class BrushField(TypedDescriptor):
  """BrushField provides a descriptor class for QBrush."""

  __field_style__ = None
  __fallback_style__ = Qt.BrushStyle.SolidPattern

  color = ColorDescriptor(Lime)

  def __init__(self, *args) -> None:
    """Initializes the descriptor. """
    TypedDescriptor.__init__(self, QBrush, self.getDefaultValue())

  def _getBrushStyle(self, ) -> Qt.BrushStyle:
    """Returns the brush style."""
    if self.__field_style__ is None:
      return self.__fallback_style__
    return self.__field_style__

  def getDefaultValue(self, ) -> QBrush:
    """Returns the default value."""
    brush = QBrush()
    brush.setColor(self.color)
    brush.setStyle(self._getBrushStyle())
    return brush
  #
  # def __get__(self, instance, owner) -> QBrush:
  #   """Returns the value of the descriptor."""
  #   if instance is None:
  #     return self
  #   color =
  #   return self.getDefaultValue()
