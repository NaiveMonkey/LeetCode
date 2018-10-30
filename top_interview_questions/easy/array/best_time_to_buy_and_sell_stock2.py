class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0

        size = len(prices)

        if size <= 1:
            return profit

        for i in range(0, size - 1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]

        return profit