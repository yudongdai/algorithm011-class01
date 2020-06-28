class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if nums == None or len(nums) <= 1:
            return
        
        n = len(nums)
        k = k % n
        i = 0
        while i < k:
            num = nums.pop()
            nums.insert(0, num)
            i += 1

# 2
