"""IntField provides a numeric descriptor class for float."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistutils.waitaminute import typeMsg

from ezdesc import TypedDescriptor


class FloatField(TypedDescriptor):
  """FloatField provides a numeric descriptor class for float."""

  def __init__(self, *args, ) -> None:
    """Initializes the descriptor. """
    for arg in args:
      if isinstance(arg, int):
        TypedDescriptor.__init__(self, float, float(arg))
      elif isinstance(arg, float):
        TypedDescriptor.__init__(self, float, arg)
      elif isinstance(arg, complex):
        if arg.imag ** 2 < 1e-10:
          TypedDescriptor.__init__(self, float, arg.real)
        elif arg.real ** 2 < 1e-10:
          TypedDescriptor.__init__(self, float, arg.imag)
    else:
      TypedDescriptor.__init__(self, float, .0)

  def __float__(self) -> float:
    """Returns the value of the descriptor."""
    return self.__default_value__
