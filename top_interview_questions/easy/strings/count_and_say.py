class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        if n == 2:
            return "11"

        count = 1
        result = "11"

        for i in range(n - 2):
            result += "S"
            temp = ""
            for j in range(len(result) - 1):
                if result[j] == result[j + 1]:
                    count += 1
                    continue

                temp += str(count) + result[j]
                count = 1

            result = temp

        return result