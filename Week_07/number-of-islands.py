class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        ans = 0
        rlen = len(grid)
        clen = len(grid[0])

        def helper(i, j):
            grid[i][j] = '0'
            for i, j in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= i < rlen and 0 <= j < clen and grid[i][j] == '1':
                    helper(i, j)

        for i in xrange(rlen):
            for j in xrange(clen):
                if grid[i][j] == '1':
                    ans += 1
                    helper(i, j) # 清除'1'
        
        return ans

# 2
