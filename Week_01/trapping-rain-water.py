class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if height == None or len(height) < 3:
            return 0

        ans = 0

        n = len(height)

        max_left = [0] * n
        max_right = [0] * n

        # 每个节点，包括自身在内的，左边最大的点
        i = 1
        max_left[0] = height[0]
        while i <= n - 2:
            max_left[i] = max(max_left[i - 1], height[i])
            i += 1

        # 每个节点，包括自身在内的，右边最大的点
        j = n - 2
        max_right[n-1] = height[n-1]
        while j >= 0:
            max_right[j] = max(max_right[j + 1], height[j])
            j -= 1

        k = 1
        while k <= n - 2:
            left = max_left[k]
            right = max_right[k]
            if min(left, right) > height[k]:
                ans += min(left, right) - height[k]
            k += 1
        
        return ans

# 4
