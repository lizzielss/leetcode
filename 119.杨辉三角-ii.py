#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (65.17%)
# Likes:    279
# Dislikes: 0
# Total Accepted:    111.7K
# Total Submissions: 171.4K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex):
        # result = [[1]]
        # current_list = [1]
        # if rowIndex == 0:
        #     return result[rowIndex]
        # for i in range(1,rowIndex+1):
        #     temp_list = []
        #     for ii in range(len(current_list)+1):
        #         if ii == 0:
        #             temp_list.append(current_list[0])
        #         elif ii == len(current_list):
        #             temp_list.append(current_list[-1])
        #         else:
        #             temp_list.append(current_list[ii-1]+current_list[ii])
        #     result.append(temp_list)
        #     current_list = temp_list
        # return result[rowIndex]
# @lc code=end

