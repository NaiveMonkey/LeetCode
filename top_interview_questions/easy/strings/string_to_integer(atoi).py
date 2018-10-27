class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        MAX_SIZE = 2147483647
        MIN_SIZE = -2147483648
        str = str.strip()
        is_negative = False

        if len(str) == 0:
            return 0

        start = 0

        if str[0] == '-':
            is_negative = True
            start += 1

        if str[0] == '+':
            start += 1

        result = ""

        for i in range(start, len(str)):
            if str[i].isdigit():
                result += str[i]
            else:
                break

        if result != "":
            result = int(result)

            if is_negative:
                result *= -1

            if result > MAX_SIZE:
                return MAX_SIZE

            if result < MIN_SIZE:
                return MIN_SIZE

            return result

        return 0