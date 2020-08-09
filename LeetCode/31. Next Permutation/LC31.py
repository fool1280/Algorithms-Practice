from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        0, 1, 2, 3, 4, 5
        1, 2, 3, 4, 5
        1, 2, 3, 5, 4
        1, 2, 4, 3, 5
        1, 2, 4, 5, 3
        1, 2, 5, 3, 4
        1, 2, 5, 4, 3
        1, 3, 2, 4, 5
        """
        
        k = len(nums) - 1
        while (k>0) and (nums[k]<=nums[k-1]):
            k = k - 1
        if (k == 0):
            for i in range(int(len(nums)/2)):
                temp = nums[i]
                nums[i] = nums[len(nums)-1-i]
                nums[len(nums)-1-i] = temp
        else:
            k = k - 1
            for i in range(len(nums)-1, k-1, -1):
                if nums[i]>nums[k]:
                    break
            temp = nums[i]
            nums[i] = nums[k]
            nums[k] = temp
            k = k + 1
            l = len(nums) - k 
            for i in range(int(l/2)):
                temp = nums[k+i]
                nums[k+i] = nums[len(nums)-1-i]
                nums[len(nums)-1-i] = temp
        return nums
    
                

res = Solution()
print(res.nextPermutation([1,5,1]))