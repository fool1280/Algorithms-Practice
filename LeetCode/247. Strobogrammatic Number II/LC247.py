from typing import List

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        number = {"1": "1", "6": "9", "9": "6", "8": "8", "0": "0"}
        it = ["1", "0", "6", "8", "9"]
        res = []
        def generateNumber(left: str, right: str, position: int):
            if position == 1:
                res.append(left + "0" + right)
                res.append(left + "1" + right)
                res.append(left + "8" + right)
                return 0
            if position == 0:
                res.append(left + right)
                return 0
            else:
                for i in it:
                    if (position == n) and (i == "0"):
                        continue
                    left1 = left + i
                    right1 = number[i] + right
                    generateNumber(left1, right1, position-2)
        if n == 0:
            return []
        elif n == 1:
            return ["0", "1", "8"]
        else:
            generateNumber("", "", n)
                
        return res
    
res = Solution()
print(res.findStrobogrammatic(3))