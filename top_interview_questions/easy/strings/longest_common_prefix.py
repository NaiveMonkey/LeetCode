class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        shortest = min(strs, key=len)
        strs.remove(shortest)

        for i, ch in enumerate(shortest):
            for compare in strs:
                if ch != compare[i]:
                    return shortest[:i]

        return shortest