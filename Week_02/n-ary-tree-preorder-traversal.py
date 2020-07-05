"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):
        if root == None:
            return

        res.append(root.val)
        if root.children:
            for c in root.children:
                self.helper(c, res)

# 3
