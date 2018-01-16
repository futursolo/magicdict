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

from typing import Iterable, TypeVar, Set

_T = TypeVar("_T")


def lower_items_reduced(obj: Iterable[_T]) -> Set[_T]:
    reduced_set: Set[_T] = set()

    for i in obj:
        try:
            i = i.lower()  # type: ignore

        except AttributeError:  # pragma: no cover
            continue

        reduced_set.add(i)

    return reduced_set


def lower_items_if_possible(obj: Iterable[_T]) -> Set[_T]:
    reduced_set: Set[_T] = set()

    for i in obj:
        try:
            i = i.lower()  # type: ignore

        except AttributeError:  # pragma: no cover
            pass

        reduced_set.add(i)

    return reduced_set
