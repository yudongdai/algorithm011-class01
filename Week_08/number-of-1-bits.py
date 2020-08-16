class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans = 0
        for _ in range(32):
            if n == 0:
                break
            if n & 1 == 1:
                ans += 1
            n = n >> 1
        return ans

# 2
