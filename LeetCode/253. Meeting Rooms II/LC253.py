from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(intervals)
        res = 0
        return res

res = Solution()
print(res.minMeetingRooms([[2,11],[6,16],[11,16]]))