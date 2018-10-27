class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size_s = len(s)
        start = 0
        end = size_s - 1

        while start < end:
            while start < end and not s[start].isalpha():
                start += 1

            while start < end and not s[end].isalpha():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True