#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (71.80%)
# Likes:    1221
# Dislikes: 0
# Total Accepted:    222.7K
# Total Submissions: 308.7K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1：
# 
# 输入：candidates = [2,3,6,7], target = 7,
# 所求解集为：
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2：
# 
# 输入：candidates = [2,3,5], target = 8,
# 所求解集为：
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
# 
# 提示：
# 
# 
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# candidate 中的每个元素都是独一无二的。
# 1 <= target <= 500
# 
# 
#

# @lc code=start
'''class Solution:
    def combinationSum(self, candidates, target):
        def caculateSub(nums,s,n):
            if s == 0:
                return True
            if nums == []:
                return 0
            result_temp = []
            for i in range(len(nums)-1,-1,-1):
                temp = []
                if s == nums[i]:
                    temp.append(s)
                if nums[i] < s:
                    nums_candidate = []
                    for ii in range(len(nums)):
                        if nums[ii]>s-nums[i]:
                            break
                        nums_candidate.append(nums[ii])
                    n+=1
                    flag = caculateSub(nums_candidate,s-nums[i],n)
                    n-=1
                    if flag:
                        # try:
                        temp = [nums[i]] + flag[0]
                        # except KeyError:
                        #     temp = temp + [nums[i]
                if temp != [] and not n:
                    result_temp.append(temp)
                if temp != [] and n:
                    result_temp = temp
                # else:
                #     n = max(n-1,0)
            return [result_temp]   
        
        result = caculateSub(candidates,target,0)
        result = [sorted(seq) for seq in result[0]]
        result_tem = result
        for i in range(len(result)):
            for j in range(i+1,len(result)):
                if result[i] == result[j]:
                    result.remove(result[j])
        return sorted(result)

a = Solution()
candidates = [1,2]
target = 4
answer = a.combinationSum(candidates,target)
print(answer)'''
'''class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx >= len(candidates) or res >= target:
                if res == target:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res + candidates[idx]) 
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, 0)
        return ans 
a = Solution()
candidates = [1,2]
target = 4
answer = a.combinationSum(candidates,target)
print(answer)'''
class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx > len(candidates)-1 or res <= 0:
                if res == 0:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res - candidates[idx]) 
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, target)
        return ans 
# @lc code=end

