#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.51%)
# Likes:    2289
# Dislikes: 0
# Total Accepted:    583.1K
# Total Submissions: 1.3M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([)]"
# 输出：false
# 
# 
# 示例 5：
# 
# 
# 输入：s = "{[]}"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s):
        kuohao_dict = {'(':')','[':']','{':'}'}
        # zuokuohao = list('([{')
        # youkuohao = list(')]}')
        s = list(s)
        temp = []
        # count = 0
        if len(s) % 2 != 0 or not s[0] in kuohao_dict.keys():
            return False
        for i in range(len(s)):
            kuohao = s[i]
            if kuohao in kuohao_dict.keys():
                temp.append(kuohao)
                # count += 1
            elif temp:
                if kuohao == kuohao_dict[temp.pop()]:
                # count -= 1
                    continue
                else:
                    return False
            else:
                return False
        if temp:
            return False
        return True
        # if count == 0:
        #     return True
        # else:
        #     return False
# a = Solution()
# s = "{[]}"
# result = a.isValid(s)
# print(result)

# @lc code=end

