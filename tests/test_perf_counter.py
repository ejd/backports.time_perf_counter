import unittest

from backports.time_perf_counter import perf_counter


class TestPerfCounter(unittest.TestCase):

    def test_perf_counter(self):
        # Verify that calling ``perf_counter()`` does not result in an
        # error.
        perf_counter()

    def test_increases(self):
        # Verify that two calls to ``perf_counter()`` return values
        # such that the second is greater than the first.  Loosely
        # based on the standard library test implemented by
        # ``test_time.TimeTestCase.test_time_ns_type()``.
        self.assertLess(perf_counter(), perf_counter())
