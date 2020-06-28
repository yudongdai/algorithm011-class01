class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if nums == None or len(nums) <= 1:
            return
        
        i = 0
        j = 1
        n = len(nums)
        while j < n:
            if nums[i] == 0 and nums[j] != 0:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
                j += 1
                continue

            if nums[i] != 0:
                i += 1
                j += 1
                continue
                
            if nums[j] == 0:
                j += 1
            
            
# 4
