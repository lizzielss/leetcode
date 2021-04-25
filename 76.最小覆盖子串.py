#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (41.20%)
# Likes:    1128
# Dislikes: 0
# Total Accepted:    130.9K
# Total Submissions: 317.4K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return t
        for size in range(len(t),len(s)+1):
            for i in range(len(s)-size+1):
                tem = s[i:i+size]
                flag = True
                for j in t:
                    if j not in tem:
                        flag = False
                        break
                if flag:
                    return tem
        return ""
# a = Solution()
# s = "abc"
# t = "ac"
# result = a.minWindow(s,t)
# print(result)
# @lc code=end

