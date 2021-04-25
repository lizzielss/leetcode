#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (64.22%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    139.6K
# Total Submissions: 218.5K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx,res):
            if idx > len(candidates) - 1 or res <= 0:
                if res == 0:
                    ans.append(temp[:])
                return 
            temp.append(candidates[idx])
            res -= candidates[idx]
            recursion(idx+1,res)
            temp.pop()
            res += candidates[idx]
            while idx<len(candidates)-1 and candidates[idx+1] == candidates[idx]:
                idx += 1
            recursion(idx+1,res)
        candidates = sorted(candidates)
        recursion(0,target)
        return ans
# a = Solution()
# candidates = [10,1,2,7,6,1,5]
# target = 8
# result = a.combinationSum2(candidates,target)
# print(result)
# @lc code=end

