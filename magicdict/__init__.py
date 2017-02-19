#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2017 Kaede Hoshikawa
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


from typing import Mapping, MutableMapping, TypeVar, KeysView, ValuesView, \
    ItemsView, Generic, Iterator, Iterable, Tuple, Any, Optional, List, Set, \
    Union

from ._version import version, __version__

import typing
import functools

__all__ = ["version", "__version__", "FrozenMagicDict", "MagicDict"]

_K = TypeVar("_K")

_V = TypeVar("_V")


class _Identifier:
    pass


_DEFAULT_MARK = _Identifier()


@functools.total_ordering
class _TotalOrdering:
    def __eq__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __lt__(self, obj: Any) -> bool:
        raise NotImplementedError


class _MagicKeysView(KeysView[_K], Generic[_K], _TotalOrdering):
    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator[_K]:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError

    def __and__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __or__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __sub__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __xor__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __reversed__(self) -> KeysView[_K]:
        raise NotImplementedError


class _MagicValuesView(ValuesView[_V], Generic[_V]):
    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator[_K]:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError

    def __eq__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __ne__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __reversed__(self) -> ValuesView[_V]:
        raise NotImplementedError


class _MagicItemsView(ItemsView[_K, _V], Generic[_K, _V], _TotalOrdering):
    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Tuple[_K, _V]]:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError

    def __and__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __or__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __sub__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __xor__(self, obj: Iterable[Any]) -> Set[Any]:
        raise NotImplementedError

    def __reversed__(self) -> ItemsView[_K, _V]:
        raise NotImplementedError


class FrozenMagicDict(Mapping[_K, _V], Generic[_K, _V]):
    def __getitem__(self, key: _K) -> _V:
        raise NotImplementedError

    def __iter__(self) -> Iterator[_K]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError

    def __eq__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __ne__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __reversed__(self) -> FrozenMagicDict[_K, _V]:
        raise NotImplementedError

    def get_first(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_last(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_iter(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_list(self, key: _K) -> List[_V]:
        raise NotImplementedError

    def copy(self) -> "FrozenMagicDict[_K, _V]":
        raise NotImplementedError

    def keys(self) -> KeysView[_K]:
        raise NotImplementedError

    def values(self) -> ValuesView[_V]:
        raise NotImplementedError

    def items(self) -> ItemsView[_K, _V]:
        raise NotImplementedError

    get = get_first
    __repr__ = __str__


class MagicDict(MutableMapping[_K, _V], Generic[_K, _V]):
    def __getitem__(self, key: _K) -> _V:
        raise NotImplementedError

    def __setitem__(self, key: _K, value: _V) -> None:
        raise NotImplementedError

    def __delitem__(self, key: _K) -> None:
        raise NotImplementedError

    def __iter__(self) -> Iterator[_K]:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __contains__(self, key: Any) -> bool:
        raise NotImplementedError

    def __eq__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __ne__(self, obj: Any) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __reversed__(self) -> FrozenMagicDict[_K, _V]:
        raise NotImplementedError

    def get_first(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_last(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_iter(self, key: _K, default: _V=None) -> Optional[_V]:
        raise NotImplementedError

    def get_list(self, key: _K) -> List[_V]:
        raise NotImplementedError

    def add(self, key: _K, value: _V) -> None:
        raise NotImplementedError

    def pop(
        self, key: _K,
            default: Union[_V, _Identifier]=_DEFAULT_MARK) -> _V:
        raise NotImplementedError

    def popitem(self) -> Tuple[_K, _V]:
        raise NotImplementedError

    def update(self, *args: Any, **kwargs: Any) -> None:  # Type Hints???
        pass

    def clear(self) -> None:
        raise NotImplementedError

    def setdefault(self, key: _K, default: _V=None) -> _V:
        raise NotImplementedError

    @classmethod
    def fromkeys(
            Cls, keys: Iterable[_K], value: _V=None) -> "MagicDict[_K, _V]":
        raise NotImplementedError

    def copy(self) -> "MagicDict[_K, _V]":
        raise NotImplementedError

    def keys(self) -> KeysView[_K]:
        raise NotImplementedError

    def values(self) -> ValuesView[_V]:
        raise NotImplementedError

    def items(self) -> ItemsView[_K, _V]:
        raise NotImplementedError

    get = get_first
    __repr__ = __str__
