#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # l = 0
        if len(set(list(s))) == 1:
            return s
        ans = []
        for i in range(len(s)):
            l = i
            r = len(s) -1
            while r >= l:
                right = r
                while l <= right and  s[l] == s[right]:
                    l += 1
                    right -= 1
                if l >= len(s):
                    l -= 1
                    right += 1
                if s[l] == s[right] and l >= right:
                    ans.append([len(s[i:r+1]),s[i:r+1]])
                    break
                r -= 1
                l = i
        if ans:
            return sorted(ans)[-1][1]
        return s[0]

# a = Solution()
# s = "ac"
# result = a.longestPalindrome(s)
# print(result)

# @lc code=end
