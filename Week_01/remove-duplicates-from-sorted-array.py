class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or len(nums) < 1:
            return 0
        
        i = 0
        j = 1
        n = len(nums)
        while j < n:
            if nums[i] == nums[j]:
                j += 1
                continue
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        return i + 1

# 3
