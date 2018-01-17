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

from typing import Reversible, ItemsView, TypeVar, Generic, Tuple, \
    Any, Set, Iterable, Iterator, AnyStr, Union

import typing
import collections

if typing.TYPE_CHECKING:  # pragma: no cover
    from .__init__ import FrozenMagicDict  # noqa: F401

__all__ = ["MagicItemsView"]

_K = TypeVar("_K")

_V = TypeVar("_V")

_T = TypeVar("_T")


def _lower_items_reduced(
        obj: Iterable[Union[_T, Tuple[AnyStr, _V]]]) -> \
            Set[Union[Tuple[AnyStr, _V]]]:
    reduced_set: Set[Tuple[AnyStr, _V]] = set()

    for i in obj:
        try:
            k, v = i  # type: ignore
            k = k.lower()

        except (AttributeError, IndexError):  # pragma: no cover
            continue

        reduced_set.add((k, v))

    return reduced_set


def _lower_items_if_possible(obj: Iterable[_T]) -> Set[_T]:
    reduced_set: Set[_T] = set()

    for i in obj:
        try:
            k, v = i  # type: ignore
            k = k.lower()

        except (AttributeError, IndexError):  # pragma: no cover
            reduced_set.add(i)

        else:
            reduced_set.add((k, v))  # type: ignore

    return reduced_set


class MagicItemsView(
        Reversible[Tuple[_K, _V]], ItemsView[_K, _V], Generic[_K, _V]):
    def __init__(self, __map: "FrozenMagicDict[_K, _V]") -> None:
        self._map = __map

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[Tuple[_K, _V]]:
        for key, value in list(self._map._kv_pairs.values()):
            yield (key, value)

    def __contains__(self, pair: Any) -> bool:
        return pair in self._map._kv_pairs.values()

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

    def __and__(self, obj: Iterable[Any]) -> Set[Tuple[_K, _V]]:
        return set(self) & set(obj)

    def __or__(self, obj: Iterable[_T]) -> Set[Union[Tuple[_K, _V], _T]]:
        return set(self) | set(obj)

    def __sub__(self, obj: Iterable[Any]) -> Set[Tuple[_K, _V]]:
        return set(self) - set(obj)

    def __xor__(self, obj: Iterable[_T]) -> Set[Union[Tuple[_K, _V], _T]]:
        return set(self) ^ set(obj)

    def __reversed__(self) -> Iterator[Tuple[_K, _V]]:
        for key, value in reversed(self._map._kv_pairs.values()):
            yield (key, value)

    def __str__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__, repr([item for item in self]))

    __repr__ = __str__


class TolerantMagicItemsView(MagicItemsView[AnyStr, _V], Generic[AnyStr, _V]):
    def __contains__(self, pair: Any) -> bool:
        try:
            lower_pair = (pair[0].lower(), pair[1])

        except (AttributeError, IndexError):  # pragma: no cover
            return False

        return super().__contains__(lower_pair)

    def __eq__(self, obj: Any) -> bool:
        try:
            lower_obj = [(k.lower(), v) for k, v in iter(obj)]

        except (AttributeError, IndexError, TypeError):  # pragma: no cover
            return False

        return super().__eq__(lower_obj)

    def __lt__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__lt__([(k.lower(), v) for k, v in iter(obj)])

        except (AttributeError, IndexError, TypeError):  # pragma: no cover
            return False

    def __le__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__le__([(k.lower(), v) for k, v in iter(obj)])

        except (AttributeError, IndexError, TypeError):  # pragma: no cover
            return False

    def __gt__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__gt__([(k.lower(), v) for k, v in iter(obj)])

        except (AttributeError, IndexError, TypeError):  # pragma: no cover
            return False

    def __ge__(self, obj: Iterable[Any]) -> bool:
        try:
            return super().__ge__([(k.lower(), v) for k, v in iter(obj)])

        except (AttributeError, IndexError, TypeError):  # pragma: no cover
            return False

    def __and__(self, obj: Iterable[Any]) -> Set[Tuple[AnyStr, _V]]:
        return super().__and__(_lower_items_reduced(obj))  # type: ignore

    def __or__(self, obj: Iterable[_T]) -> Set[Union[Tuple[AnyStr, _V], _T]]:
        return super().__or__(_lower_items_if_possible(obj))  # type: ignore

    def __sub__(self, obj: Iterable[Any]) -> Set[Tuple[AnyStr, _V]]:
        return super().__sub__(_lower_items_reduced(obj))  # type: ignore

    def __xor__(self, obj: Iterable[_T]) -> Set[Union[Tuple[AnyStr, _V], _T]]:
        return super().__xor__(_lower_items_if_possible(obj))  # type: ignore
