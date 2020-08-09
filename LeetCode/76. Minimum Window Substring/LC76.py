from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = Counter(t)
        len_check = len(list(check))
        current = {}
        left = 0
        right = 0
        len_current = 0
        ans = False, 0, 0
        minLength = len(s)+1
        while right<len(s):
            c = s[right]
            current[c] = current.get(c, 0) + 1
            if (c in check) and (current[c] == check[c]):
                len_current += 1
            if len_current >= len_check:
                if len_current == len_check and right-left+1<minLength:
                    ans = True, left, right
                    minLength = right-left+1
                while left<=right and len_current>=len_check:
                    c = s[left]
                    current[c] -= 1
                    left += 1
                    if (c in check) and (current[c]<check[c]):
                        len_current  -= 1
                    if current[c] == 0:
                        del current[c]
                    if len_current == len_check and right-left+1<minLength:
                        ans = True, left, right
                        minLength = right-left+1
            right += 1
        if ans[0]:
            return s[ans[1]:ans[2]+1]
        else:
            return ""
        
res = Solution()
print(res.minWindow("aa", "aa"))