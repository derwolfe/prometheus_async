# Copyright 2016 Hynek Schlawack
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

try:
    import asyncio
except ImportError:
    asyncio = None

import time

import pytest
import six

from prometheus_async import _util


py2_only = pytest.mark.skipif(six.PY3, reason="Python 2-only test.")
py3_only = pytest.mark.skipif(six.PY2, reason="Python 3-only test.")


class TestMkTime(object):
    @py2_only
    def test_py2(self):
        """
        Use monotonic.time on Python 2
        """
        import monotonic
        assert (
            _util.get_time is
            monotonic.time is
            _util.mk_get_time()
        )

    @py3_only
    def test_py3(self):
        """
        Use time.perf_counter on Python 3
        """
        assert (
            _util.get_time is
            time.perf_counter is
            _util.mk_get_time()
        )
