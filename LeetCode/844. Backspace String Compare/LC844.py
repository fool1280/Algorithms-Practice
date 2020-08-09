class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        for i in range(len(S)):
            c = S[i]
            if c != "#":
                s.append(c)
            else:
                if len(s):
                    s.pop()
        t = []
        for i in range(len(T)):
            c = T[i]
            if c != "#":
                t.append(c)
            else:
                if len(t):
                    t.pop()
        return (s == t)

res = Solution()
print(res.backspaceCompare("a#c", "b"))