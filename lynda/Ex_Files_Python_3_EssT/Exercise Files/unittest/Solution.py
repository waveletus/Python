class Solution(object):
    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        listStr = list(s)
        for i in range(len(s)):
            listStr[l - i - 1] = s[i]

        return ''.join(listStr)

    def reverseString2(self, s):
        return s[::-1]

    def reverseString3(self, s):
        return self.reverse(list(s), 0, len(s) - 1)

    def reverse(self, s, low, high):
        if (low >= high):
            return "".join(s)

        s[low], s[high] = s[high], s[low]
        return self.reverse(s, low + 1, high - 1)

    def reverseString4(self, s):
        return ''.join(reversed(list(s)))

    def reverseString5(self, s):
        n = len(s)
        s = list(s)
        for i in range(int(n/2)):
            s[i], s[~i] = s[~i], s[i]

        return ''.join(s)