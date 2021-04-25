#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (38.25%)
# Likes:    868
# Dislikes: 0
# Total Accepted:    110.7K
# Total Submissions: 286.1K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 示例:
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 说明:
# 
# 假设你总是可以到达数组的最后一个位置。
# 
#

# @lc code=start
class Solution:
    def jump(self, nums):
        temp = []
        result = []
        def recursion(idx):
            if idx >= len(nums) - 1 or idx < 0:
                if idx == len(nums) - 1:
                    result.append(len(temp))
                    return True
                return False
            step = nums[idx]
            temp.append(step)
            idx += step
            if step>0:
                recursion(idx)
            else:
                temp.pop()
                return False
            idx -= step
            while step > 1:
                temp.pop()
                step -= 1
                temp.append(step)
                idx += step
                if recursion(idx):
                    temp.pop()
                    break
                idx -= step
            else:
                temp.pop()
                return False
        recursion(0)
        return min(result)
a = Solution()
nums = [2,3,1,1,4]
result = a.jump(nums)
# print(result)
# @lc code=end

