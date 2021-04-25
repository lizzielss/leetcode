#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (41.49%)
# Likes:    1115
# Dislikes: 0
# Total Accepted:    214.1K
# Total Submissions: 511.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个下标。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums):
        result = []
        def subfunction(index):
            if result:
                return
            if index >= len(nums) - 1:
                # if index == len(nums) - 1:
                result.append(True)
                return 
            step = nums[index]
            index += step
            if step > 0:
                subfunction(index)
            if result:
                return
            index -= step
            while step > 1:
                step -= 1
                index += step
                if index >= len(nums):
                    result.append(True)
                    return
                subfunction(index)
                index -= step
            
        subfunction(0)
        if result:
            return True
        return False  


a = Solution()
nums = [3,2,1,0,4]
result = a.canJump(nums)
print(result)
                
# @lc code=end

