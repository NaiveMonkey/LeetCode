class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minimum = -2147483648
        maximum = 2147483648
        is_minus = False
        if x < 0:
            is_minus = True
            str_x = str(abs(x))
        else:
            str_x = str(x)
        size = len(str_x)
        result = 0
        for i in range(size):
            if i > 0:
                result *= 10
            result += int(str_x[size - i - 1])

        if is_minus:
            result *= -1
        if result > maximum or result < minimum:
            return 0
        return result

    def reverseOther(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        neg = False
        if x < 0:  # append negative later
            x = 0 - x
            neg = True

        while x > 0:
            rem = x % 10
            x = (int)(x / 10)
            ret *= 10  # ok because ret starts at 0
            ret += rem

        # special cases
        if ret > 2147483647:  # case where reversed number larger than 2^31 - 1
            return 0
        if neg == True:
            ret *= -1

        return ret