class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = dict()
        for num in nums:
            distinct[num] = distinct.get(num, 0) + 1

        for k, v in distinct.items():
            if v == 1:
                return k