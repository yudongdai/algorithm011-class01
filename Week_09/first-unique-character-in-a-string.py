class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {}
        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        
        for i in xrange(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1

# 1
