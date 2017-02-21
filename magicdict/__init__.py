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
    Union, Dict, MappingView, Reversible

from ._version import version, __version__

import threading
import collections
import threading
import collections.abc
import abc

__all__ = ["version", "__version__", "FrozenMagicDict", "MagicDict"]

_K = TypeVar("_K")

_V = TypeVar("_V")


class _Identifier:
    pass


_DEFAULT_MARK = _Identifier()


class _MagicKeysView(KeysView[_K], Generic[_K]):
    def __init__(self, map: Union["FrozenMagicDict", "MagicDict"]) -> None:
        self._map = map

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[_K]:
        for key, _ in list(self._map._kv_pairs.values()):
            yield key

    def __contains__(self, key: Any) -> bool:
        return key in self._map._pair_ids.keys()

    def __eq__(self, obj: Any) -> bool:
        if hasattr(obj, "__reversed__") and callable(obj.__reversed__):
            # If an object can be reversed, then it should have an order.
            return list(self) == list(obj)

        else:
            return set(self) == set(obj)

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __lt__(self, obj: Any) -> bool:
        return set(self) < set(obj)

    def __le__(self, obj: Any) -> bool:
        return set(self) <= set(obj)

    def __gt__(self, obj: Any) -> bool:
        return set(self) > set(obj)

    def __ge__(self, obj: Any) -> bool:
        return set(self) >= set(obj)

    def __and__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) & set(obj)

    def __or__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) | set(obj)

    def __sub__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) - set(obj)

    def __xor__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) ^ set(obj)

    def __reversed__(self) -> KeysView[_K]:
        return reversed(self._map).keys()  # type: ignore


class _MagicValuesView(ValuesView[_V], Generic[_V]):
    def __init__(self, map: Union["FrozenMagicDict", "MagicDict"]) -> None:
        self._map = map

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
        if hasattr(obj, "__reversed__") and callable(obj.__reversed__):
            # If an object can be reversed, then it should have an order.
            return list(self) == list(obj)

        else:
            return set(self) == set(obj)

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __reversed__(self) -> ValuesView[_V]:
        return reversed(self._map).values()  # type: ignore


class _MagicItemsView(
        Reversible[Tuple[_K, _V]], ItemsView[_K, _V], Generic[_K, _V]):
    def __init__(self, map: Union["FrozenMagicDict", "MagicDict"]) -> None:
        self._map = map

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[Tuple[_K, _V]]:
        for key, value in list(self._map._kv_pairs.values()):
            yield (key, value)

    def __contains__(self, pair: Any) -> bool:
        return pair in self._map._kv_pairs.values()

    def __eq__(self, obj: Any) -> bool:
        if hasattr(obj, "__reversed__") and callable(obj.__reversed__):
            # If an object can be reversed, then it should have an order.
            return list(self) == list(obj)

        else:
            return set(self) == set(obj)

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __lt__(self, obj: Any) -> bool:
        return set(self) < set(obj)

    def __le__(self, obj: Any) -> bool:
        return set(self) <= set(obj)

    def __gt__(self, obj: Any) -> bool:
        return set(self) > set(obj)

    def __ge__(self, obj: Any) -> bool:
        return set(self) >= set(obj)

    def __and__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) & set(obj)

    def __or__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) | set(obj)

    def __sub__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) - set(obj)

    def __xor__(self, obj: Iterable[Any]) -> Set[Any]:
        return set(self) ^ set(obj)

    def __reversed__(self) -> Iterator[Tuple[_K, _V]]:
        return reversed(self._map).items()  # type: ignore


class FrozenMagicDict(Reversible[_K], Mapping[_K, _V], Generic[_K, _V]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._pair_ids: Dict[_K, List[_Identifier]] = {}
        self._kv_pairs: \
            "collections.OrderedDict[_Identifier, Tuple[_K, _V]]" = \
            collections.OrderedDict()

        def add_one(key: _K, value: _V) -> None:
            identifier = _Identifier()

            if key not in self.keys():
                self._pair_ids[key] = [identifier]

            else:
                self._pair_ids[key].append(identifier)

            self._kv_pairs[identifier] = (key, value)

        if len(args):
            if len(args) > 1:  # pragma: no cover
                raise TypeError(
                    ("update expected at most 1 positional argument, "
                     "got {} args.").format(len(args)))

            else:
                if isinstance(args[0], collections.abc.Mapping):
                    for k, v in args[0].items():
                        add_one(k, v)

                elif isinstance(args[0], collections.abc.Iterable):
                    for k, v in args[0]:
                        add_one(k, v)

                else:  # pragma: no cover
                    raise TypeError(
                        ("update expected a Mapping or an Iterable "
                         "as the positional argument, got {}.")
                        .format(type(args[0])))

        for k, v in kwargs.items():
            add_one(k, v)

    def __getitem__(self, key: _K) -> _V:
        identifier = self._pair_ids[key][0]
        _, value = self._kv_pairs[identifier]
        return value

    def __iter__(self) -> Iterator[_K]:
        return iter(self.keys())

    def __len__(self) -> int:
        return len(self._kv_pairs)

    def __contains__(self, key: Any) -> bool:
        return key in self._pair_ids

    def __eq__(self, obj: Any) -> bool:
        if isinstance(obj, collections.abc.Mapping):
            return self.items() == obj.items()

        if isinstance(obj, collections.abc.Iterable):
            return self.items() == obj

        return False

    def __ne__(self, obj: Any) -> bool:
        return not self.__eq__(obj)

    def __str__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__,
            repr([(key, value) for (key, value) in self.items()]))

    def __reversed__(self) -> Iterator[_K]:
        return self.__class__(reversed(list(self.items())))

    def get_first(self, key: _K, default: Optional[_V]=None) -> Optional[_V]:
        if key not in self.keys():
            return default

        return self[key]

    def get_last(self, key: _K, default: Optional[_V]=None) -> Optional[_V]:
        if key not in self.keys():
            return default

        identifier = self._pair_ids[key][-1]
        _, value = self._kv_pairs[identifier]
        return value

    def get_iter(self, key: _K) -> Iterator[_V]:
        for identifier in self._pair_ids.get(key, []):
            _, value = self._kv_pairs[identifier]

            yield value

    def get_list(self, key: _K) -> List[_V]:
        return list(self.get_iter(key))

    def copy(self) -> "FrozenMagicDict[_K, _V]":
        return self.__class__(self)

    def keys(self) -> _MagicKeysView[_K]:
        return _MagicKeysView(self)

    def values(self) -> _MagicValuesView[_V]:
        return _MagicValuesView(self)

    def items(self) -> _MagicItemsView[_K, _V]:
        return _MagicItemsView(self)

    get = get_first
    __repr__ = __str__


class MagicDict(
        FrozenMagicDict[_K, _V], MutableMapping[_K, _V], Generic[_K, _V]):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._lock = threading.Lock()

        FrozenMagicDict.__init__(self, *args, **kwargs)

    def __getitem__(self, key: _K) -> _V:
        with self._lock:
            identifier = self._pair_ids[key][0]
            _, value = self._kv_pairs[identifier]
            return value

    def __setitem__(self, key: _K, value: _V) -> None:
        if key in self.keys():
            del self[key]

        identifier = _Identifier()

        with self._lock:
            self._pair_ids[key] = [identifier]
            self._kv_pairs[identifier] = (key, value)

    def __delitem__(self, key: _K) -> None:
        with self._lock:
            ids = self._pair_ids.pop(key)
            for identifier in ids:
                del self._kv_pairs[identifier]

    def get_last(self, key: _K, default: Optional[_V]=None) -> Optional[_V]:
        if key not in self.keys():
            return default

        with self._lock:
            identifier = self._pair_ids[key][-1]
            _, value = self._kv_pairs[identifier]
            return value

    def get_iter(self, key: _K) -> Iterator[_V]:
        with self._lock:
            vals = [
                self._kv_pairs[identifier][1]
                for identifier in self._pair_ids.get(key, [])]

        for val in vals:
            yield val

    def add(self, key: _K, value: _V) -> None:
        if key in self.keys():
            identifier = _Identifier()

            with self._lock:
                self._pair_ids[key].append(identifier)
                self._kv_pairs[identifier] = (key, value)

        else:
            self[key] = value

    def pop(
        self, key: _K,
            default: Union[_V, _Identifier]=_DEFAULT_MARK) -> _V:
        if key not in self.keys():
            if default is _DEFAULT_MARK:
                raise KeyError(key)

            else:
                return default  # type: ignore

        with self._lock:
            identifier = self._pair_ids[key].pop()

            if len(self._pair_ids[key]) == 0:
                del self._pair_ids[key]

            _, value = self._kv_pairs.pop(identifier)

            return value

    def popitem(self) -> Tuple[_K, _V]:
        with self._lock:
            identifier, pair = self._kv_pairs.popitem()

            key, _ = pair

            self._pair_ids[key].remove(identifier)

            if len(self._pair_ids[key]) == 0:
                del self._pair_ids[key]

            return pair

    def update(self, *args: Any, **kwargs: Any) -> None:  # Type Hints???
        if len(args):
            if len(args) > 1:
                raise TypeError(
                    ("update expected at most 1 positional argument, "
                     "got {} args.").format(len(args)))

            else:
                if isinstance(args[0], collections.abc.Mapping):
                    for k, v in args[0].items():
                        self.add(k, v)

                elif isinstance(args[0], collections.abc.Iterable):
                    for k, v in args[0]:
                        self.add(k, v)

                else:
                    raise TypeError(
                        ("update expected a Mapping or an Iterable "
                         "as the positional argument, got {}.")
                        .format(type(args[0])))

        for k, v in kwargs.items():
            self.add(k, v)

    def clear(self) -> None:
        with self._lock:
            self._kv_pairs.clear()
            self._pair_ids.clear()

    def setdefault(self, key: _K, default: _V=None) -> _V:
        if key in self.keys():
            return self[key]

        self[key] = default  # type: ignore
        return default  # type: ignore

    @classmethod
    def fromkeys(
            Cls, keys: Iterable[_K], value: _V=None) -> "MagicDict[_K, _V]":
        magic_dict: MagicDict[_K, _V] = Cls()

        for key in keys:
            magic_dict.add(key, value)  # type: ignore

        return magic_dict

    def copy(self) -> "MagicDict[_K, _V]":
        return self.__class__(self)
