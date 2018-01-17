#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2018 Kaede Hoshikawa
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

from typing import ValuesView, Generic, Union, Iterator, Any, TypeVar

import typing
import collections

if typing.TYPE_CHECKING:
    from .__init__ import FrozenMagicDict  # noqa: F401

__all__ = ["MagicValuesView"]

_V = TypeVar("_V")

_T = TypeVar("_T")


class MagicValuesView(ValuesView[_V], Generic[_V]):
    def __init__(self, __map: Union["FrozenMagicDict[Any, _V]"]) -> None:
        self._map = __map

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[_V]:
        for _, value in list(self._map._kv_pairs.values()):
            yield value

    def __contains__(self, value: Any) -> bool:
        for _, _value in list(self._map._kv_pairs.values()):
            if _value == value:
                return True

        else:
            return False

    def __eq__(self, obj: Any) -> bool:
        if not isinstance(obj, collections.abc.Iterable):  # pragma: no cover
            return False

        return list(self) == list(obj)

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __reversed__(self) -> Iterator[_V]:
        for _, value in reversed(self._map._kv_pairs.values()):
            yield value

    def __str__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__, repr([item for item in self]))

    __repr__ = __str__
