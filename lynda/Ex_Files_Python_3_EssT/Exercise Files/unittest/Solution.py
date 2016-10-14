class Solution(object):
    # def reverseString(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     l = len(s)
    #     listStr = list(s)
    #     for i in range(len(s)):
    #         listStr[l-i-1] = s[i]

    #     return ''.join(listStr)

    # def reverseString(self, s):
    #     return s[::-1]

    def reverseString(self, s):
        return self.reverse(list(s), 0, len(s) - 1)

    def reverse(self, s, low, high):
        if (low >= high):
            return "".join(s)

        s[low], s[high] = s[high], s[low]
        return self.reverse(s, low + 1, high - 1)


def main():
    print(Solution().reverseString("abc dfad"))