#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (39.58%)
# Likes:    763
# Dislikes: 0
# Total Accepted:    320K
# Total Submissions: 805.8K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack, needle):
        '''
        haystack = list(haystack)
        needle = list(needle)
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        index = 0
        flag = []
        # for s in needle:
        while index < len(haystack):
            for s in needle:
                if haystack[index] == s: 
                    flag.append([index,s])
                    index += 1
                    # break
                if flag:
                    index = 
                index += 1
        if flag:
            return flag[0]
        else:
            return -1
        '''
        if not needle or needle==haystack:
            return 0
        if len(needle) > len(haystack):
            return -1
        window = len(needle)
        for i in range(len(haystack)-window+1):
            if haystack[i:i+window]==needle:
                return i
            # else:
            #     continue
        return -1
a = Solution()
haystack = "abc"
needle = "c"
result = a.strStr(haystack,needle)
print(result)
# @lc code=end

