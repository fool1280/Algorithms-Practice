from typing import List

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        current = 0
        t = list(zip(indexes, sources, targets))
        t = sorted(t, key=lambda x: x[0])
        print(t)
        for i in range(len(t)):
            while current<t[i][0]:
                res += S[current]
                current += 1
            temp = S[current:current+len(t[i][1])]
            if temp == t[i][1]:
                res += t[i][2] 
            else:
                res += temp
            current = current + len(t[i][1])
        res += S[current:]
        return res
    
res = Solution()
print(res.findReplaceString("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]))