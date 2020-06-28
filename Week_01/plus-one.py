class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits == None:
            return None
        n = len(digits) - 1
        digits[n] += 1
        while n >= 0:
            if digits[n] <= 9:
                n -= 1
                continue
            if n > 0:
                digits[n] = 0
                digits[n - 1] += 1
            else:
                digits[n] = 0
            n -= 1
        
        if digits[0] == 0:
            digits.insert(0, 1)
        
        return digits
# 2
