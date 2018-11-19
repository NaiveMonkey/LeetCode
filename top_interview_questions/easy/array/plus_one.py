class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = 0
        for num in digits:
            result *= 10
            result += num

        result += 1
        answer = list()

        while result > 0:
            print(result)
            rem = int(result % 10)
            result = int(result // 10)
            answer.insert(0, rem)

        return answer