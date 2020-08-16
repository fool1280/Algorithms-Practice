from typing import List

class Solution:
    def swap(self, a, b, c, d):
        return d, a, b, c
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        rank = n // 2
        for i in range(rank):
            #matrix[i][i], matrix[i][n-1-i], matrix[n-1-i][n-1-i], matrix[n-1-i][i]
            for j in range(n-1-i*2):
                #matrix[i][i+j], matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i]
                matrix[i][i+j], matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i] = self.swap(matrix[i][i+j], matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i])
        return matrix

res = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
res.rotate(matrix)
for i in matrix:
    print(i)
