#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (30.23%)
# Likes:    2828
# Dislikes: 0
# Total Accepted:    383.3K
# Total Submissions: 1.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
# 
# 注意：答案中不可以包含重复的三元组。
# 
# 
# 
# 示例：
# 
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    '''my answer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        nums.sort()
        for i in range(len(nums)):
            temp = []
            for j in range(i+1,len(nums)):
                if nums[j] in temp:
                    # r = sorted([nums[i],nums[j],0-nums[i]-nums[j]])
                    r = [nums[i],nums[j],0-nums[i]-nums[j]] 
                    r.sort()
                    if r not in result:
                        result.append(r)
                else:
                    c = 0 - nums[i] - nums[j]
                    temp.append(c)
        return result
    '''
    def threeSum(self, nums):
        res = []
        nums.sort() #从小到大排序
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  #跳过重复的值，保证最后的结果唯一
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:   #和太小，把最小的值变大一点
                    l +=1 
                elif s > 0:     #和太大，把最大的值变小一点
                    r -= 1
                else:       #和为0，记录下
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:   #跳过左边有重复的值
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   #跳过右边有重复的值
                        r -= 1
                    l += 1; r -= 1
        return res

# a = Solution()
# nums = [-1, 0, 1, 2, -1, -4]
# a.threeSum(nums)

# @lc code=end

