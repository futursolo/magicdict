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


class MagicValuesViewTestCase:
    def test_method_len(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert len(dic.values()) == 4

    def test_method_iter(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert list(iter(dic.values())) == ["b", "d", "d", "f"]

    def test_method_contains(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert "b" in dic.values()
        assert "g" not in dic.values()

    def test_method_eq_ne(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert dic.values() == [v for _, v in sample]

        assert dic.values() != []

    def test_method_reversed(self):
        sample = [("a", "b"), ("c", "d"), ("c", "d"), ("e", "f")]
        dic = FrozenMagicDict(sample)

        assert list(reversed(dic.values())) == \
            list(reversed([v for _, v in sample]))

    def test_method_str(self):
        dic = FrozenMagicDict([("a", "b")])

        assert str(dic.values()) == "MagicValuesView(['b'])"