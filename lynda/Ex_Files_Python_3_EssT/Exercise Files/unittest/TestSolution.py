import unittest
from . import Solution

class TestSolution(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(Solution.Solution().reverseString1("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString1("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString1("a x "), " x a", "miss match")

        self.assertEqual(Solution.Solution().reverseString2("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString2("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString2("a x "), " x a", "miss match")

        self.assertEqual(Solution.Solution().reverseString3("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString3("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString3("a x "), " x a", "miss match")

        self.assertEqual(Solution.Solution().reverseString4("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString4("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString4("a x "), " x a", "miss match")

        self.assertEqual(Solution.Solution().reverseString5("abc"), "cba", "miss match")
        self.assertEqual(Solution.Solution().reverseString5("abcd"), "dcba", "miss match")
        self.assertEqual(Solution.Solution().reverseString5("a x "), " x a", "miss match")