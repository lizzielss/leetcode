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
        # 方法一
        # if s == t:
        #     return t
        # target_dict = {}
        # for st in t:
        #     try:
        #         target_dict[st] += 1
        #     except:
        #         target_dict[st] = 1
        # for size in range(len(t),len(s)+1):
        #     for i in range(len(s)-size+1):
                # tem = s[i:i+size] #窗口内容
        #         temp_dict = target_dict.copy()
        #         # flag = True
        #         for j in tem:
        #             if j in temp_dict.keys():
        #                 temp_dict[j] -= 1
        #                 # break
        #         # if sorted(temp_dict.items(),key=lambda x:x[1],reverse=True)[0][1] <= 0:
        #         if max(temp_dict.values()) <= 0:
        #             return tem
        # return ""
        # 方法二
        # if s == t:
        #     return t
        # target_dict = {}
        # min_len = 1e5
        # result = ""
        # for st in t:
        #     try:
        #         target_dict[st] += 1
        #     except:
        #         target_dict[st] = 1
        # dict_list = target_dict.keys()
        # for left in range(len(s)-len(t)+1):
        #     if s[left] not in dict_list:
        #         continue
        #     # if len(s) - left < len(t):
        #     #     continue
        #     temp_dict = target_dict.copy()
        #     right = left
        #     flag = True
        #     while True:
        #         # temp = s[:right]
        #         if s[right] in dict_list:
        #             temp_dict[s[right]] -= 1
        #         right += 1
        #         # if sorted(temp_dict.items(),key=lambda x:x[1],reverse=True)[0][1] <= 0:
        #         if right - left >= len(t):
        #             if max(temp_dict.values()) <= 0:
        #                 flag = False
        #                 right -= 1
        #                 break
        #         if right == len(s):
        #             break
        #     if flag:
        #         break
        #     # left = 0
        #     # right -= 1
        #     # while True:
        #     #     if s[left] in temp_dict.keys():
        #     #         break
        #     #     left += 1
        #     if right+1-left < min_len:
        #         min_len = right+1-left
        #         result = s[left:right+1]
        # return result
        # 方法三
        target_dict = {}
        for st in t:
            try:
                target_dict[st] += 1
            except:
                target_dict[st] = 1
        # if len(s) == len(t) and s != t:
        #     return ""
        left, right = 0, len(t) - 1
        min_len = 1e5
        result = ""

        while right < len(s) and left < len(s) - len(t) + 1:
            while right < len(s):
                temp_dict = target_dict.copy()
                for ss in s[left:right+1]:
                    if ss in temp_dict.keys():
                        temp_dict[ss] -= 1
                if max(temp_dict.values()) <= 0:
                    if len(s[left:right+1]) < min_len:
                        min_len = len(s[left:right+1])
                        result = s[left:right+1]
                    right += 1
                    break
                right += 1
            if max(temp_dict.values()) > 0:
                break
            while left < len(s) - len(t) + 1:
                if temp_dict == target_dict:
                    break
                try:
                    temp_dict[s[left]] += 1
                except:
                    pass
                if max(temp_dict.values()) > 0:
                    if len(s[left:right]) < min_len:
                        min_len = len(s[left:right])
                        result = s[left:right]
                    left += 1
                    break
                left += 1
            if temp_dict == target_dict:
                break
        return result

a = Solution()
s = "babb"
t = "baba"
result = a.minWindow(s,t)
print(result)
# @lc code=end

