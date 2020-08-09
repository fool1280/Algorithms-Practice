from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = start + ((end-start) // 2)
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                res = mid
                break
            if A[mid]>A[mid-1]:
                start = mid + 1
            else:
                end = mid - 1
                
        return res
    
res = Solution()
print(res.peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))