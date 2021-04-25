#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.83%)
# Likes:    650
# Dislikes: 0
# Total Accepted:    175.8K
# Total Submissions: 383.6K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        
        temp = pow(10,4)
        res = []   
        for i in range(len(nums)-2):
            a = pow(10,4)
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                dif = abs(target - s)
                if dif <= a:
                    a = dif
                else:
                    res.append([abs(target-temp),temp])
                if target - s > 0:
                    l += 1
                elif target - s < 0:
                    r -= 1
                else:
                    return s
                temp = s
            res.append([dif,temp])
        res.sort()       
        return res[0][1]
# s = Solution()
# nums = [87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4]
# target = -275
# s.threeSumClosest(nums,target)

# @lc code=end

