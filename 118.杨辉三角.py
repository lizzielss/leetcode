#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (70.60%)
# Likes:    479
# Dislikes: 0
# Total Accepted:    164.7K
# Total Submissions: 233.2K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows):
        result = [[1]]
        current_list = [1]
        for i in range(1,numRows):
            temp_list = []
            for ii in range(len(current_list)+1):
                if ii == 0:
                    temp_list.append(current_list[0])
                elif ii == len(current_list):
                    temp_list.append(current_list[-1])
                else:
                    temp_list.append(current_list[ii-1]+current_list[ii])
            result.append(temp_list)
            current_list = temp_list
        return result
a = Solution()
numRows = 33
result = a.generate(numRows)
print(result)
# @lc code=end

