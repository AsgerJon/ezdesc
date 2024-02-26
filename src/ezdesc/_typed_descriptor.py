"""TypedDescriptor provides strongly typed descriptor functionality. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from vistutils.waitaminute import typeMsg

from ezdesc._abstract_descriptor import AbstractDescriptor


class TypedDescriptor(AbstractDescriptor):
  """TypedDescriptor provides strongly typed descriptor functionality. """

  @staticmethod
  def _parseTypeArg(type_: type, arg: Any) -> dict:
    return dict(type_=type_, defVal=arg)

  @staticmethod
  def _parseType(type_: type) -> dict:
    """Parses single type arg"""
    return dict(type_=type_, defVal=None)

  @staticmethod
  def _parseArg(arg: Any) -> dict:
    """Parses single non-type arg"""
    return dict(type_=type(arg), defVal=arg)

  def __init__(self, *args) -> None:
    """Initializes the descriptor. """
    parsed = None
    if not args:
      raise ValueError('Missing arguments')
    if len(args) == 1 and isinstance(args[0], type):
      parsed = self._parseType(*args)
    elif len(args) == 1 and args[0] is not None:
      parsed = self._parseArg(*args)
    elif len(args) == 1:
      raise ValueError('Missing Arguments!')
    elif len(args) == 2 and isinstance(args[0], type):
      if isinstance(args[1], args[0]):
        parsed = self._parseTypeArg(args[0], args[1])
      else:
        e = typeMsg('arg', args[1], args[0])
        raise TypeError(e)
    elif len(args) == 2 and isinstance(args[1], type):
      if isinstance(args[0], args[1]):
        parsed = self._parseTypeArg(args[1], args[0])
      else:
        e = typeMsg('arg', args[0], args[1])
        raise TypeError(e)
    if parsed is None:
      raise ValueError('Missing Arguments')
    if isinstance(parsed, dict):
      if parsed.get('type_') is None:
        raise ValueError('Missing Arguments')
    else:
      e = typeMsg('parsed', parsed, dict)
      raise TypeError(e)
    type_ = parsed.get('type_', )
    if not isinstance(type_, type):
      e = typeMsg('type_', type_, type)
      raise TypeError(e)
    self.__field_type__ = type_
    self.__default_value__ = parsed.get('defVal')

  def __set__(self, instance, value) -> None:
    """This method is called to set the value of the field. """
    if not isinstance(value, self.__field_type__):
      e = typeMsg('value', value, self.__field_type__)
      raise TypeError(e)
    pvtName = self._getPrivateName()
    setattr(instance, pvtName, value)

  def _getFieldType(self) -> type:
    """Returns the type of the field. """
    return self.__field_type__
