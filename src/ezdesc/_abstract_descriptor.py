"""AbstractDescriptor is the base class for all descriptors in the
library. It provides the logic that carries the original instance through
the nested descriptors. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Any


class AbstractDescriptor:
  """AbstractDescriptor is the base class for all descriptors in the
  library. It provides the logic that carries the original instance through
  the nested descriptors. """

  __field_name__ = None
  __field_owner__ = None
  __field_temp_instance__ = None
  __default_value__ = None
  __field_type__ = None

  def __set_name__(self, owner: type, name: str) -> None:
    """This method is automatically called when the owner class is
    created. In particular, if the owner class were created with a custom
    metaclass, this method is called after mcls.__new__ has returned,
    but before mcls.__init__ is called. Thus, when used in the context of
    metaclasses, the __init__ method can be expected to occur after
    __set_name__ has been called on all descriptor instances. """
    self.__field_name__ = name
    self.__field_owner__ = owner
    self.__field_temp_instance__ = None

  def setTempInstance(self, instance: Any, ) -> None:
    """Sets the temporary instance. """
    self.__field_temp_instance__ = instance

  def getTempInstance(self) -> Any:
    """Returns the temporary instance. """
    if self.__field_temp_instance__ is None:
      return self
    if isinstance(self.__field_temp_instance__, AbstractDescriptor):
      return self.__field_temp_instance__.getTempInstance()
    return self, self.__field_temp_instance__,

  def _getPrivateName(self) -> str:
    """Returns the private name of the field. """
    fieldName = '_%s' % self.__field_name__
    return fieldName
    # instance = self.getTempInstance()

  def __get__(self, instance: Any, owner: type) -> Any:
    """This method is called to get the value of the field. """
    if instance is None:
      return self
    if isinstance(instance, AbstractDescriptor):
      return self.__get__(instance.getTempInstance(), owner)
    pvtName = self._getPrivateName()
    out = getattr(instance, pvtName)
    if isinstance(out, AbstractDescriptor):
      out.setTempInstance(instance)
    return out

  def __set__(self, instance: Any, value: Any) -> None:
    """This method is called to set the value of the field. """
    if isinstance(instance, AbstractDescriptor):
      instance.__set__(instance.getTempInstance(), value)
    pvtName = self._getPrivateName()
    setattr(instance, pvtName, value)

  @abstractmethod
  def _getFieldType(self) -> type:
    """Returns the type of the field. """
