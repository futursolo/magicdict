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

from magicdict import FrozenMagicDict


class MagicItemsViewTestCase:
    def test_method_len(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert len(dic.items()) == 4

    def test_method_iter(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert list(iter(dic.items())) == sample

    def test_method_contains(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert ("a", "b") in dic.items()
        assert ("b", "b") not in dic.items()

    def test_method_eq_ne(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert dic.items() == sample

        assert dic.items() != []

    def test_method_reversed(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert reversed(dic.items()) == reversed(sample)

    def test_method_lt(self):
        sample = [("a", "b"), ("c", "d")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d"), ("e", "f")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() <= dic2.items()

    def test_method_le(self):
        sample = [("a", "b"), ("c", "d")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d"), ("e", "f")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() < dic2.items()

    def test_method_gt(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() > dic2.items()

    def test_method_ge(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() >= dic2.items()

    def test_method_and(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() & dic2.items() == set([("a", "b"), ("c", "d")])

    def test_method_or(self):
        sample = [("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() | dic2.items() == set(
            [("a", "b"), ("c", "d"), ("e", "f")])

    def test_method_sub(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() - dic2.items() == set([("e", "f")])

    def test_method_xor(self):
        sample = [("a", "b"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        sample2 = [("a", "b"), ("c", "d")]
        dic2 = FrozenMagicDict(sample2)

        assert dic.items() ^ dic2.items() == set([("e", "f")])

    def test_method_str(self):
        dic = FrozenMagicDict([("a", "b")])

        assert str(dic.items()) == "_MagicItemsView([('a', 'b')])"
