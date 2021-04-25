#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (39.06%)
# Likes:    638
# Dislikes: 0
# Total Accepted:    283K
# Total Submissions: 721.4K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        y = (l+r) // 2
        flag = 1
        while flag:
            if y*y <= x and (y+1)*(y+1) > x:
                break
            elif y*y > x:
                r = y
            else:
                l = y
            y = (l+r) // 2
        return y

# a = Solution()
# x = 1
# result = a.mySqrt(x)
# print(result)
# @lc code=end

