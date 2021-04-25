#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.06%)
# Likes:    903
# Dislikes: 0
# Total Accepted:    222.2K
# Total Submissions: 525.2K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
# 
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 
# 进阶：
# 
# 
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 
# 示例 2：
# 
# 
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 
# 示例 3：
# 
# 
# 输入：nums = [], target = 0
# 输出：[-1,-1]
# 
# 
# 
# 提示：
# 
# 
# 0 
# -10^9 
# nums 是一个非递减数组
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums, target):
        '''l, r = 0, len(nums) - 1
        strat_index, end_index = None, None

        # if len(nums) == 1 and target == nums[0]:
        #     return [0,0]
        # elif len(nums) == 1 and target != nums[0]:
        #     return [-1,-1]
        
        while l <= r:
            mid = (l + r) // 2
            # if mid == 0:
            #     if nums[0] == target:
            #         strat_index = 0
            #         l = 1
            #         continue
            #     else:
            #         l = 1
                
            # if mid == len(nums) - 1:
            #     if nums[len(nums)-1] == target:
            #         end_index = len(nums) - 1
            #         r = len(nums) - 2
            #         continue
            #     else:
            #         r = len(nums) - 2
            #     # continue
            if nums[mid] == target:
                if mid == len(nums) -1 or nums[mid + 1] != target:
                    end_index = mid
                    r = mid - 1
            # elif nums[mid] == target:
                elif mid == 0 or nums[mid - 1] != target:
                    strat_index = mid
                    l = mid + 1
            else:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

        if  strat_index==None and end_index==None:
            return [-1,-1]
        
        return [strat_index,end_index]'''
        left = 0
        right = len(nums) - 1
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                firstIndex = mid - 1
                lastIndex = mid + 1
                while firstIndex >= 0 and nums[firstIndex] == target:
                    firstIndex -= 1
                while lastIndex < len(nums) and nums[lastIndex] == target:
                    lastIndex += 1
                return [firstIndex+1, lastIndex-1]
        return [-1, -1]
if __name__ == '__main__':
    nums = [2,2,2]
    target = 2
    s = Solution()
    result = s.searchRange(nums,target)
# @lc code=end

