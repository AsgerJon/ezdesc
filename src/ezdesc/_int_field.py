"""IntField provides a numeric descriptor class for int."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ezdesc import TypedDescriptor


class IntField(TypedDescriptor):
  """IntField provides a numeric descriptor class for int."""

  def __init__(self, *args, ) -> None:
    """Initializes the descriptor. """
    for arg in args:
      if isinstance(arg, int):
        TypedDescriptor.__init__(self, int, arg)
      elif isinstance(arg, float):
        if arg.is_integer():
          TypedDescriptor.__init__(self, int, int(arg))
      elif isinstance(arg, complex):
        if arg.imag ** 2 < 1e-10:
          if arg.real.is_integer():
            TypedDescriptor.__init__(self, int, int(arg.real))
        elif arg.real ** 2 < 1e-10:
          if arg.imag.is_integer():
            TypedDescriptor.__init__(self, int, int(arg.imag))
    else:
      TypedDescriptor.__init__(self, int, 0)

  def __int__(self) -> int:
    """Returns the value of the descriptor."""
    return self.__default_value__
