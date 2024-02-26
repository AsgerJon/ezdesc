"""AbstractNumericField provides an abstract baseclass for strongly typed
numeric descriptors. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod

from vistutils.waitaminute import typeMsg

from ezdesc import TypedDescriptor


class AbstractNumericField(TypedDescriptor):
  """AbstractNumericField provides an abstract baseclass for strongly typed
  numeric descriptors. """

  @abstractmethod
  def __init__(self, *args) -> None:
    """Initializes the descriptor. """
    TypedDescriptor.__init__(self, *args)
