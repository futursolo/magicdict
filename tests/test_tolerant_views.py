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

from magicdict import FrozenTolerantMagicDict


class TolerantMagicKeysViewTestCase:
    def test_method_contains(self):
        sample = [("A", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert "a" in dic.keys()
        assert "A" in dic.keys()
        assert "d" not in dic.keys()

    def test_method_eq_ne(self):
        sample = [("A", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert dic.keys() == [k.lower() for k, _ in sample]

        assert dic.keys() != []

    def test_method_reversed(self):
        sample = [("A", "b"), ("c", "d"), ("C", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert reversed(dic.keys()) == reversed([k.lower() for k, _ in sample])

    def test_method_lt(self):
        sample = [("a", "b"), ("c", "d")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("A", "b"), ("c", "d"), ("e", "f")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() <= dic2.keys()

    def test_method_le(self):
        sample = [("a", "b"), ("c", "d")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("A", "b"), ("c", "d"), ("e", "f")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() < dic2.keys()

    def test_method_gt(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("A", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() > dic2.keys()

    def test_method_ge(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() >= dic2.keys()

    def test_method_and(self):
        sample = [("a", "b"), ("C", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() & dic2.keys() == set(["a", "c"])

    def test_method_or(self):
        sample = [("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("C", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() | dic2.keys() == set(["a", "c", "e"])

    def test_method_sub(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("C", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() - dic2.keys() == set(["e"])

    def test_method_xor(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("A", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.keys() ^ dic2.keys() == set(["e"])


class TolerantMagicItemsViewTestCase:
    def test_method_contains(self):
        sample = [("A", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert ("a", "b") in dic.items()
        assert ("B", "b") not in dic.items()

    def test_method_eq_ne(self):
        sample = [("A", "b"), ("C", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert dic.items() == [(k.upper(), v) for k, v in sample]

        assert dic.items() != []

    def test_method_reversed(self):
        sample = [("a", "b"), ("C", "d"), ("c", "d"), ("E", "f")]
        dic = FrozenTolerantMagicDict(sample)

        assert reversed(
            dic.items()) == reversed([(k.lower(), v) for k, v in sample])

    def test_method_lt(self):
        sample = [("a", "b"), ("C", "d")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d"), ("e", "f")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() <= dic2.items()

    def test_method_le(self):
        sample = [("a", "b"), ("c", "d")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("C", "d"), ("e", "f")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() < dic2.items()

    def test_method_gt(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("A", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() > dic2.items()

    def test_method_ge(self):
        sample = [("a", "b"), ("c", "d"), ("E", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() >= dic2.items()

    def test_method_and(self):
        sample = [("a", "b"), ("C", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() & dic2.items() == set([("a", "b"), ("c", "d")])

    def test_method_or(self):
        sample = [("c", "d"), ("E", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("C", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() | dic2.items() == set(
            [("a", "b"), ("c", "d"), ("e", "f")])

    def test_method_sub(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() - dic2.items() == set([("e", "f")])

    def test_method_xor(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenTolerantMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenTolerantMagicDict(sample2)

        assert dic.items() ^ dic2.items() == set([("e", "f")])
