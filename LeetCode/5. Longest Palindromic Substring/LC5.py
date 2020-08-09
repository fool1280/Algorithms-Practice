class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        if s[j] != s[i]
        f[i][j] = max(f[i+1][j], f[i][j-1])
        
        => Have to compute f[i+1][j] and f[i][j-1] first 
        => Compute by length
        0 1
        1 2 
        3 4
        0 2 
        1 
        """
        f =[[0 for j in range(len(s))] for i in range(len(s))]
        res = 0
        start = 0
        end = 0
        for i in range(len(s)):
            f[i][i] = True
            
        for i in range(1, len(s)):
            for j in range(len(s)-i):
                k = j + i
                if k-j == 1 and s[k] == s[j]:
                    f[j][k] = True
                else:
                    f[j][k] = f[j+1][k-1] and (s[j] == s[k])
                    
                if f[j][k] and k-j+1>res:
                    res = k-j+1
                    start = j
                    end = k
        return s[start:end+1]
                
        
res = Solution()
print(res.longestPalindrome("abba"))