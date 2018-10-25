class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_size = len(s)
        t_size = len(t)

        if s_size != t_size:
            return False

        list_s = list(s)
        list_t = list(t)
        list_s.sort()
        list_t.sort()

        if list_s != list_t:
            return False

        '''
        Second Solution (I think this is more appropriate for coding interview)        
        s_size = len(s)
        t_size = len(t)

        if s_size != t_size:
            return False

        anagram_dict = dict()

        for string in s:
            if string not in anagram_dict:
                anagram_dict[string] = 1
            else:
                anagram_dict[string] += 1

        for string in t:
            if string not in anagram_dict:
                return False

            value = anagram_dict[string]
            if value == 0:
                return False

            anagram_dict[string] -= 1

        return True
        
        '''

        return True
