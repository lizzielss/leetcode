#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix = list(zip(*matrix[::-1]))
        # print(matrix)
        return matrix
a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = a.rotate(matrix)
print(result)
# @lc code=end

