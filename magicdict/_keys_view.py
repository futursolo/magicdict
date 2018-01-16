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

from typing import \
    Iterator, KeysView, Generic, Union, Iterable, Set, Any, Reversible, \
    AnyStr, TypeVar

from ._utils import lower_items_reduced, lower_items_if_possible

import typing
import collections

if typing.TYPE_CHECKING:  # pragma: no cover
    from .__init__ import FrozenMagicDict, MagicDict  # noqa: F401

__all__ = ["MagicKeysView"]

_K = TypeVar("_K")

_V = TypeVar("_V")

_T = TypeVar("_T")


class MagicKeysView(KeysView[_K], Reversible[_K], Generic[_K]):
    def __init__(self, __map: "MagicDict[_K, _V]") -> None:
        self._map = __map

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[_K]:
        for key, _ in self._map._kv_pairs.values():
            yield key

    def __contains__(self, key: Any) -> bool:
        return key in self._map._pair_ids.keys()

    def __eq__(self, obj: Any) -> bool:
        if not isinstance(obj, collections.abc.Iterable):  # pragma: no cover
            return False

        return list(self) == list(obj)

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __lt__(self, obj: Iterable[Any]) -> bool:
        return set(self) < set(obj)

    def __le__(self, obj: Iterable[Any]) -> bool:
        return set(self) <= set(obj)

    def __gt__(self, obj: Iterable[Any]) -> bool:
        return set(self) > set(obj)

    def __ge__(self, obj: Iterable[Any]) -> bool:
        return set(self) >= set(obj)

    def __and__(self, obj: Iterable[Any]) -> Set[_K]:
        return set(self) & set(obj)

    def __or__(self, obj: Iterable[_T]) -> Set[Union[_K, _T]]:
        return set(self) | set(obj)

    def __sub__(self, obj: Iterable[Any]) -> Set[_K]:
        return set(self) - set(obj)

    def __xor__(self, obj: Iterable[_T]) -> Set[Union[_K, _T]]:
        return set(self) ^ set(obj)

    def __reversed__(self) -> Iterator[_K]:
        for key, _ in reversed(self._map._kv_pairs.values()):
            yield key

    def __str__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__, repr([item for item in self]))

    __repr__ = __str__


class TolerantMagicKeysView(
        MagicKeysView[AnyStr], Generic[AnyStr]):
    def __contains__(self, key: Any) -> bool:
        try:
            return super().__contains__(key.lower())

        except AttributeError:  # pragma: no cover
            return False

    def __eq__(self, obj: Any) -> bool:
        if not isinstance(obj, collections.abc.Iterable):  # pragma: no cover
            return False

        try:
            lower_obj = [item.lower() for item in iter(obj)]

        except (AttributeError, TypeError):  # pragma: no cover
            return False

        return super().__eq__(lower_obj)

    def __lt__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__lt__([item.lower() for item in iter(obj)])

        except (AttributeError, TypeError):  # pragma: no cover
            return False

    def __le__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__le__([item.lower() for item in iter(obj)])

        except (AttributeError, TypeError):  # pragma: no cover
            return False

    def __gt__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__gt__([item.lower() for item in iter(obj)])

        except (AttributeError, TypeError):  # pragma: no cover
            return False

    def __ge__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__ge__([item.lower() for item in iter(obj)])

        except (AttributeError, TypeError):  # pragma: no cover
            return False

    def __and__(self, obj: Iterable[Any]) -> Set[AnyStr]:
        return super().__and__(lower_items_reduced(obj))  # type: ignore

    def __or__(self, obj: Iterable[_T]) -> Set[
            Union[AnyStr, _T]]:
        return super().__or__(lower_items_if_possible(obj))  # type: ignore

    def __sub__(self, obj: Iterable[Any]) -> Set[AnyStr]:
        return super().__sub__(lower_items_reduced(obj))  # type: ignore

    def __xor__(self, obj: Iterable[_T]) -> Set[Union[AnyStr, _T]]:
        return super().__xor__(lower_items_if_possible(obj))  # type: ignore

    def __reversed__(self) -> Iterator[AnyStr]:
        return super().__reversed__()  # type: ignore
