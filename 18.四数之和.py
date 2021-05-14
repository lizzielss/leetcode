#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target: int) :
        nums.sort()
        res = []
        if len(nums) == 4:
            if sum(nums) == target:
                return [nums]
            else:
                return []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:    #跳过重复的
                continue
            l, m, r = i + 1, i + 2, len(nums) - 1
            while l < r :
                while m < r:
                    s = nums[i] + nums[l] + nums[m] + nums[r] 
                    if target - s > 0:
                        while nums[m]==nums[m+1]:
                            if m < len(nums)-2:         #跳过重复
                                m += 1
                            else:
                                break
                        m += 1
                        continue
                    if target -s < 0:
                        while nums[r]==nums[r-1]:
                            r -= 1
                        r -= 1
                        continue
                    if target -s == 0:
                        res.append([nums[i], nums[l], nums[m], nums[r]])
                        while nums[m]==nums[m+1]:
                            if m < len(nums)-2:
                                m+= 1
                            else:
                                break
                        m += 1
                        continue
                while nums[l]==nums[l+1] :
                    if l < len(nums)-2:
                        l += 1
                    else:
                        break
                l += 1
                m = l + 1
                r = len(nums) - 1
                
        return res

a  = Solution()
nums =  [0,-1,-3,5,-5]
target = 1
a.fourSum(nums,target)

# @lc code=end

