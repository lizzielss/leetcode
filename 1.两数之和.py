#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i 
            else:
                return map[num[i]], i 

        return -1, -1
# @lc code=end

