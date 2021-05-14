#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start


'''
输入初始排序的数组{
       1.如果数组长度为1或者为0
              直接返回数组
       2.如果数组长度为2
              直接交换数组中两个值的位置
              返回交换后的数组
       3.从最后一个值开始向前查找（循环1）
                 如果[这个值]比[前一个值]大（判断）
                        从最后往前查找截止到[这个值]（循环2）
                                   如果出现有值大于[前一个值]（判断）
                                           交换这两个值的位置
                                           跳出循环2
                        遍历这个值的后一个值到末位（循环）
                                数字从两边分别交换数值，一直到中间
                        返回数组
       4.排除前面三种情况，说明排序已经是从前往后是最大值
          遍历从前到中间的位置(循环)
                 数字从两边分别交换数值，一直到中间
          返回数组
}
'''
# class Solution:
    # def nextPermutation(self, nums):
        # """
        # # Do not return anything, modify nums in-place instead.
        # """
''' my code 
        a = nums[0]
        m = nums[0]
        index = 0
        for i in range(1,len(nums)):
            if a <= nums[i]:
                a = nums[i]
            elif m > nums[i]:
                m = nums[i]
                index = i
        nums[0], nums[index]= m, nums[0]
        # b = nums[1]
        # for j in range(1,len(nums)-1):
            # if nums[j] < b:
                # nums[]
        for i in range(len(nums) - 2):  # 这个循环负责设置冒泡排序进行的次数
            for j in range(1,len(nums) - i - 1):  # j为列表下标
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
'''
'''
方法一
'''
class Solution:
    def nextPermutation(self, nums):
        l = len(nums)
        index = 0
        if l == 1 or l ==0:
            None
        elif l == 2 and nums[0] < nums[1]:
            nums[0],nums[1] = nums[1],nums[0]
        else:
            a = nums[0]
            for i in range(l-1,-1,-1):
                if nums[i]>nums[i-1]:
                    a = nums[i-1]
                    index = i-1
                    break
            for i in range(l-1,-1,-1): 
                if nums[i] > a:
                    nums[index], nums[i] = nums[i], a
                    break
            for i in range(l-index-2):
                for j in range(index+1,  l-1):
                    if nums[j] > nums[j +1]:
                        nums[j],nums[j      +1] = nums[j+1],    nums[j]
                    # break






a = Solution()
nums = [3,2,1]
a.nextPermutation(nums)
# @lc code=end

