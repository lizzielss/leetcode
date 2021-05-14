#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums.remove(val)
                if l < len(nums):
                    continue
            if l == len(nums):
                break
            else:
                l += 1
                r = len(nums) - 1

a = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
a.removeElement(nums,val)

# @lc code=end

