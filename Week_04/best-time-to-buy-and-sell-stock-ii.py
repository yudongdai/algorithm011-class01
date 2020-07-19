class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices == None or len(prices) <= 1:
            return 0

        i = 1
        n = len(prices)
        ans = 0
        while i < n:
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]
            i += 1
        return ans
# 2
