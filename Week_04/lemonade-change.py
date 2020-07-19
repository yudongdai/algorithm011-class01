class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        r = {}
        r[5] = 0
        r[10] = 0

        for b in bills:
            if b == 5:
                r[5] += 1
                continue
            
            if b == 10:
                if r[5] >= 1:
                    r[5] -= 1
                    r[10] += 1
                else:
                    return False
            elif b == 20:
                if r[10] >= 1 and r[5] >= 1:
                    r[5] -= 1
                    r[10] -= 1
                elif r[5] >= 3:
                    r[5] -= 3
                else:
                    return False
            else:
                return False
        
        return True

