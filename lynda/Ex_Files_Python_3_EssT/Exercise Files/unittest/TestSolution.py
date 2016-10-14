import unittest
from . import Solution

class TestSolution(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Solution.Solution().reverseString("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString("a x "), " x a", "miss match")
