class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        num_map = dict()
        point = 0
        counting = 0
        for i in range(size):
            if nums[i] in num_map:
                counting += 1
                continue
            num_map[nums[i]] = nums[i]
            temps = nums[i]
            nums[i] = nums[point]
            nums[point] = temps

            point += 1

        del nums[size - counting:]

        return len(nums)