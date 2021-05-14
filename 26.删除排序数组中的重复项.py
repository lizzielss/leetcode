#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) :
        nums.sort()
        l = len(nums)   #记录原始列表的长度
        for i in range(l):
            l1 = len(nums)
            if l1 == i + 1: #已经遍历到最后一个元素
                return l1
            target = nums[i]    
            j = i + 1
            while nums[j] == target:
                nums.remove(target)
                if len(nums) == j:
                    return len(nums)
        return len(nums)

a =  Solution()
nums = [1,1,2,2,2,3,3]
a.removeDuplicates(nums)
# @lc code=end

