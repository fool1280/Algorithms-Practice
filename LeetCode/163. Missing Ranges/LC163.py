from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        previous, current = None, None
        res = []
        for i in range(len(nums)):
            current = nums[i]
            if previous is None:
                previous = lower
                if current - previous>0:
                    if current - previous == 1:
                        res.append(str(previous))
                    else:
                        res.append(str(previous) + "->" + str(current-1))
            else:
                if current - previous >= 2:
                    if current - previous == 2:
                        res.append(str(previous+1))
                    else:
                        res.append(str(previous+1) + "->" + str(current-1)) 
            previous = current
        previous = current
        current = upper
        if previous is None:
            previous = lower
            if current - previous > 0:
                res.append(str(previous) + "->" + str(current))
            else:
                res.append(str(previous))
        elif current - previous > 0:
            if current - previous == 1:
                res.append(str(current))
            else:
                res.append(str(previous+1) + "->" + str(current))
        return res
    
res = Solution()
print(res.findMissingRanges([-1], -1, 0))