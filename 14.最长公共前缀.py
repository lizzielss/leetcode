#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (39.03%)
# Likes:    1534
# Dislikes: 0
# Total Accepted:    483.7K
# Total Submissions: 1.2M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs):
        flag = 1
        length = 0
        common = ''
        while flag:
            # if length == 0:
            try:
                s = strs[0][length]
                for i in range(1,len(strs)):
                    if strs[i][length] == s:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag:
                    common += s
                    length += 1
            except IndexError:
                return common
        return common

# a = Solution()
# strs = ["flower","flow","flight"]
# result = a.longestCommonPrefix(strs)
# print(result)
# @lc code=end

