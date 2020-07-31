from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        res = 0
        while (start<=end):
            res = max(res, min(height[start], height[end])*(end-start))
            if height[start]>=height[end]:
                end -= 1
            else:
                start += 1
        return res
            
    
res = Solution()
print(res.maxArea([1,8,6,2,5,4,8,3,7]))