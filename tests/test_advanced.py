# -*- coding: utf-8 -*-

from context import solutions

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        solutions.hmm()


if __name__ == '__main__':
    unittest.main()
