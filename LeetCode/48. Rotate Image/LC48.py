from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

res = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
res.rotate(matrix)
for i in matrix:
    print(i)
