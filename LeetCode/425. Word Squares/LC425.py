from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        AnagramDict = {}
        for word in words:
            for i in range(len(word)):
                current = word[:i+1]
                if current not in AnagramDict:
                    AnagramDict[current] = set([word])
                else:
                    AnagramDict[current].add(word)
        res = []
        def getWords(prefix: str):
            if prefix in AnagramDict: 
                return(AnagramDict[prefix])
            else:
                return(set())
            
        def ArrangeWords(current: List[str], position: int):
            if position == len(words[0]):
                res.append(current.copy())
                return 0
            else:
                prefix = ""
                for i in range(len(current)):
                    prefix = prefix + current[i][position]
                check = getWords(prefix)
                for word in check:
                    current.append(word)
                    ArrangeWords(current, position+1)
                    current.pop()
                        
        for word in words:
            ArrangeWords([word], 1)
        return res
        
res = Solution()
print(res.wordSquares(["abat","baba","atan","atal"]))