#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (47.11%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    222.3K
# Total Submissions: 471.9K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower().strip()
        new_string = ""
        if string == "":
            return True
        for s in string:
            if s.isalpha() or s.isdigit():
                new_string+=s
        if new_string[::-1] == new_string:
            return True
        else:
            return False
# @lc code=end

