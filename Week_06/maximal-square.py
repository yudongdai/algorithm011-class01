class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # 重复子问题
        # 状态数组
        # 状态转移方程
        # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        if len(matrix) ==0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        imax = 0
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":
                    continue
                
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                
                imax = max(imax, dp[i][j])
        
        return imax * imax

    # 1
