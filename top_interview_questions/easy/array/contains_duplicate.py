class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        distinct = dict()
        for i in range(len(nums)):
            if nums[i] in distinct:
                return True
            distinct[nums[i]] = nums[i]

        return False