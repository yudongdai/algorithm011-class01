class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        ln = len(s)
        i = 0
        while i < ln:
            self.helper(s, i, min(i + k, ln) - 1)
            i += 2 * k
        return "".join(s)

    def helper(self, s, left, right):
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
