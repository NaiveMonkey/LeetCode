class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []

        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1

        res = []
        for i in nums2:
            if i in dict1:
                if dict1[i] > 0:
                    dict1[i] = dict1[i] - 1
                    res.append(i)

        return res