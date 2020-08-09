from collections import Counter, deque
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        current = deque([])
        count = Counter()
        for i in range(len(s)):
            current.append(s[i])
            if s[i] not in count:
                count[s[i]] = 1
            else: 
                count[s[i]] += 1
            if len(count.keys())<=2:
                res = max(res, sum(count.values()))
            else:
                while len(count.keys())>2:
                    x = current.popleft()
                    if count[x]>1:
                        count[x] -= 1
                    else:
                        del count[x]
        return res
        
res = Solution()
print(res.lengthOfLongestSubstringTwoDistinct("ccaabbb"))