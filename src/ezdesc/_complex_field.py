"""ComplexField class for complex numbers."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ezdesc import TypedDescriptor


class ComplexField(TypedDescriptor):
  """ComplexField provides a numeric descriptor class for complex."""

  def __init__(self, *args, ) -> None:
    """Initializes the descriptor. """
    for arg in args:
      if isinstance(arg, (int, float, complex)):
        TypedDescriptor.__init__(self, complex, arg + 0j)
    else:
      TypedDescriptor.__init__(self, complex, 0j)

  def __complex__(self) -> complex:
    """Returns the value of the descriptor."""
    return self.__default_value__
