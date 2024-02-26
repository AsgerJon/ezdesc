"""The 'ezdesc' provides easy implementation of nested descriptors. This
is particularly useful when working with complex nested data structures.
The main motivation however was to simplify development of complex widgets
in PySide6."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from ._abstract_descriptor import AbstractDescriptor
from ._typed_descriptor import TypedDescriptor
from ._abstract_numeric_field import AbstractNumericField
from ._int_field import IntField
from ._float_field import FloatField
from ._complex_field import ComplexField
from ._color_descriptor import ColorDescriptor
from ._brush_field import BrushField
