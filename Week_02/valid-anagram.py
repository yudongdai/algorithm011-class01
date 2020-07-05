class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == None or t == None:
            return False
        
        hashmap = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                 hashmap[c] += 1

        for c in t:
            if c not in hashmap:
                return False
            else:
                 hashmap[c] -= 1

        for _, v in hashmap.items():
            if v != 0:
                return False
        
        return True


# 3
