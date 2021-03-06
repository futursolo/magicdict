#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2021 Kaede Hoshikawa
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from . import (
    _dict,
    _frozen_dict,
    _frozen_tolerant_dict,
    _items_view,
    _keys_view,
    _tolerant_dict,
    _values_view,
    _version,
)
from ._dict import MagicDict  # noqa: F401
from ._frozen_dict import FrozenMagicDict  # noqa: F401
from ._frozen_tolerant_dict import FrozenTolerantMagicDict  # noqa: F401
from ._items_view import MagicItemsView  # noqa: F401
from ._keys_view import MagicKeysView  # noqa: F401
from ._tolerant_dict import TolerantMagicDict  # noqa: F401
from ._values_view import MagicValuesView  # noqa: F401
from ._version import __version__  # noqa: F401

__all__ = (
    _version.__all__
    + _keys_view.__all__
    + _values_view.__all__
    + _items_view.__all__
    + _frozen_dict.__all__
    + _frozen_tolerant_dict.__all__
    + _dict.__all__
    + _tolerant_dict.__all__
)
