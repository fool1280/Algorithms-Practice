from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        preMax = []
        suffMax = []
        for i in range(len(height)):
            if (i == 0):
                current = height[i]
            else:
                current = max(current, height[i])
            preMax.append(current)
        for j in range(len(height)-1, -1, -1):
            if (j == len(height) - 1):
                current = height[j]
            else:
                current = max(current, height[j])
            suffMax.insert(0, current)
        currMax = 0
        for i in range(len(height)):
            currMax += min(preMax[i], suffMax[i]) - height[i]
        return currMax
        """
        res = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                h = height[stack.pop()]
                if not stack:
                    break
                res += (min(height[i], height[stack[-1]]) - h) * (i - stack[-1] - 1)
            stack.append(i)
        return res

res = Solution()
print(res.trap([0, 5, 4, 2, 4]))