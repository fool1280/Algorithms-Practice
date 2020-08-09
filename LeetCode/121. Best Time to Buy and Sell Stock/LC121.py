from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        fmin = []
        fmax = []
        for i in range(len(prices)):
            fmax.append(0)
            if i == 0:
                fmin.append(prices[i])
            else:
                fmin.append(min(prices[i], fmin[-1]))
        for i in range(len(prices)-1, -1, -1):
            if i == len(prices)-1:
                fmax[i] = prices[i]
            else:
                fmax[i] = max(prices[i], fmax[i+1])
        for i in range(len(prices)):
            res = max(res, fmax[i] - fmin[i])
        return res
        
res = Solution()
print(res.maxProfit([7,6,4,3,1]))