#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (34.85%)
# Likes:    2617
# Dislikes: 0
# Total Accepted:    619.9K
# Total Submissions: 1.8M
# Testcase Example:  '123'
#
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：x = 123
# 输出：321
# 
# 
# 示例 2：
# 
# 
# 输入：x = -123
# 输出：-321
# 
# 
# 示例 3：
# 
# 
# 输入：x = 120
# 输出：21
# 
# 
# 示例 4：
# 
# 
# 输入：x = 0
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# -2^31 
# 
# 
#

# @lc code=start
'''class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        y = list(str(y))
        y = y[::-1]
        y = int(''.join(y))
        if x < 0:
            return -y
        return y'''

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        x1 = abs(x)
        while(x1!=0):
            temp = x1%10
            if res > 214748364 or (res==214748364 and temp>7):
                return 0
            if res<-214748364 or (res==-214748364 and temp<-8):
                return 0
            res = res*10 +temp
            x1 //=10
        return res if x >0 else -res

# @lc code=end

                        