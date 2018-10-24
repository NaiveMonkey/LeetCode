class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        result = ""
        for i in range(size):
            result += s[size - i - 1]

        return result