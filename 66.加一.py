#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (45.58%)
# Likes:    654
# Dislikes: 0
# Total Accepted:    269.6K
# Total Submissions: 590.3K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
# 
# 
# 示例 2：
# 
# 
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 
# 
# 示例 3：
# 
# 
# 输入：digits = [0]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        # if digits[-1] == 9:
        #     try:
        #         digits[-2] += 1
        #         digits[-1] = 0
        #     except IndexError:
        #         digits = [1,0]
        # else:
        #     digits[-1] += 1
        # return digits
        index = len(digits) - 1
        while index >= 0:
            if digits[index] + 1 > 9:
                digits[index] = 0
                if index == 0:
                    digits = [1] + digits
                    return digits
                index -= 1
            else:
                digits[index] += 1
                # break
                return digits

# a = Solution()
# digits = [9,9]
# result = a.plusOne(digits)
# print(result)
# @lc code=end

