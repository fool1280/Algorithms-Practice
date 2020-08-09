from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortNum = sorted(range(len(nums)), key=lambda k: nums[k])
        left = 0
        right = len(nums)-1
        while left<=right:
            x = nums[sortNum[left]] + nums[sortNum[right]]
            if x == target:
                return [sortNum[left], sortNum[right]]
            elif x>target:
                right -= 1
            else:
                left += 1
            
res = Solution()
print(res.twoSum(nums = [2, 2, 3, 2], target = 4))
                