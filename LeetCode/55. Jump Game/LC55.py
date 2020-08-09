class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        """
        end = 0 + nums[0]
        for i in range(1, len(nums)):
            if (i>end):
                return False
            else:
                end = max(end, i + nums[i])
        return True
    
res = Solution()
print(res.canJump([1, 1, 2, 3, 0, 0, 4]))