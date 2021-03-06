#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (51.16%)
# Likes:    1598
# Dislikes: 0
# Total Accepted:    418.3K
# Total Submissions: 807.7K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    # 增加缓存装饰器
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        '''
        def subfunction(m):
            if m < 0:
                return 
            if m == 0:
                global count
                count = count + 1
            else:
                subfunction(m-1)
                subfunction(m-2)
            return
        
        global count
        count = 0
        subfunction(n)
        return count
        '''
        return self.climbStairs(n-1) + self.climbStairs(n-2) if n > 2 else n
# n = 3
# a = Solution()
# result = a.climbStairs(n)
# print(result)
# @lc code=end

