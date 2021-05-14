#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        result = []
        temp = ''
        while r < len(s):
            while r < len(s) and len(set(temp)) == len(temp):
                temp = temp + s[r]
                r += 1
            if r != len(s):
                temp = list(temp)
                temp.pop()
                temp = ''.join(temp)
                result.append([len(temp), temp])
                temp += s[r-1]
            else:
                if len(set(temp)) == len(temp):
                    result.append([len(temp), temp])
                else:
                    temp = list(temp)
                    temp.pop()
                    temp = ''.join(temp)
                    result.append([len(temp), temp])
                    temp += s[r - 1]
            while l <= r and len(set(temp)) != len(temp):
                l += 1
                temp = s[l:r ]
        result = sorted(result, key=lambda x: x[0], reverse=True)
        print(result)
        return result[0][1]

a = Solution()
s = "pwwkew"
result = a.lengthOfLongestSubstring(s)
print(result)

# @lc code=end
