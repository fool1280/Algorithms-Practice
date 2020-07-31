from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1) New interval merge
        2) Add new interval
        3) Merge with existing intervals
        """
        res = []
        check = True
        for i in range(len(intervals)):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                if newInterval[1]<intervals[i][0]:
                    if check:
                        res.append(newInterval)
                        res.append(intervals[i])
                        check = False
                    else:
                        res.append(intervals[i])
                else:
                    #intervals[i][1]>=newInterval[0]
                    #intervals[i][0]<=newIntervals[1]
                    newInterval[0] = min(newInterval[0], intervals[i][0])
                    newInterval[1] = max(newInterval[1], intervals[i][1])
                    continue
        if check:
            res.append(newInterval)
        return res
                
                

res = Solution()
print(res.insert([[1,3],[6,9]], [2,5]))