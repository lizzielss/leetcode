#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (54.40%)
# Likes:    597
# Dislikes: 0
# Total Accepted:    160.6K
# Total Submissions: 295.3K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = "0" * (len(a)-len(b)) + b
            l = len(a)
        else:
            a = "0" * (len(b)-len(a)) + a
            l = len(b)
        flag = 0
        ans = ""
        for i in range(l - 1,-1,-1):
            if a[i] == "1" and b[i] == "1":
                if flag:
                    ans = "1" + ans 
                else:
                    ans = "0" + ans
                flag = 1
            if (a[i] == "1" and b[i] == "0") or (b[i] == "1" and a[i] == "0"):
                if flag:
                    ans = "0" + ans
                else:
                    ans = "1"  + ans
            if a[i] == "0" and b[i] == "0":
                if flag:
                    ans = "1"  + ans
                else:
                    ans = "0" + ans
                flag = 0
        if flag:
            ans = "1" + ans
        return ans    

# a = "1010"
# b = "1011"
# aa = Solution()
# result = aa.addBinary(a, b)
# print(result)
# @lc code=end

