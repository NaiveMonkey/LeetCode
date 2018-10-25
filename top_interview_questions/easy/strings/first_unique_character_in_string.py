import sys

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_map = dict()
        sort_list = list()
        size = len(s)
        if size < 1:
            return -1
        for i in range(size):
            if s[i] in unique_map:
                unique_map[s[i]] = sys.maxsize
                continue

            unique_map[s[i]] = i

        for k, v in unique_map.items():
            sort_list.append(v)
        sort_list.sort()
        if sort_list[0] == sys.maxsize:
            return -1
        return sort_list[0]


    def firstUniqCharOther(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = list()

        for string in s:
            if string not in str_list:
                str_list.append(string)

        for string in str_list:
            if s.count(string) == 1:
                return s.index(string)

        return -1


