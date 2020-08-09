class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(0, 0, n, "", res)
        return res
        
    def helper(self, left, right, n, s, res):

        if left == n and right == n:
            res.append(s)
            return
        
        if left < n:
            self.helper(left + 1, right, n, s+"(", res)

        if right < left:
            self.helper(left, right + 1, n, s+")", res)  

# 3
