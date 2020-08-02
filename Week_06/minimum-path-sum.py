class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 重复子问题
        # 状态数组
        # 状态转移方程  
        # i>0, j>0 dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]

        # n行 m列

        n = len(grid)
        m = len(grid[0])
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                    continue
                if i == 0:
                    dp[0][j] = dp[0][j - 1] + grid[i][j]
                    continue
                if j == 0:
                    dp[i][0] = dp[i - 1][0] + grid[i][j]
                    continue
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        
        return dp[n- 1][m -1]

# 1
