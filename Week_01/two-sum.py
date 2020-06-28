class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == None or len(nums) <= 1:
            return None
        
        i = 0
        n = len(nums)
        hashmap = {}
        while i < n:
            hashmap[nums[i]] = i
            i += 1
        
        i = 0
        while i < n:
            r = target - nums[i]
            if r in hashmap and hashmap[r] != i:
                return[i, hashmap[r]]
            i += 1
        return None

# 3
