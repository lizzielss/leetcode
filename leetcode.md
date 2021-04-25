[TOC]



## 31.下一个排列

笔记:
排列是有顺序的,从小到大是最小排列,下一个排列则是不符合从小到大的顺序.
如果要找下一个排列,从列表的末尾去找,然后将不符合从大到小的规律的拿出来交换.并且把交换后的子列表逆序排序成从小到大.

## 33.搜索旋转排序数组
笔记:
排序数组首先想到二分查找,因为经过旋转,必定有一边是有序的,根据一边的首尾判断是否是有序,然后根据target是否出现在有序的那边,确定下一次查找的区域.

## 34.在排序数组中查找元素的第一个和最后一个位置
==需要重做==
没有考虑好边界条件,不能面向数据集的编程

## 35.搜索插入位置
较简单,可以学习一下别人的做法

## 39.组合总和

![https://assets.leetcode-cn.com/solution-static/39/39_fig1.png](leetcode.assets/39_fig1.png)

```python
class Solution:
    def combinationSum(self, candidates, target):
        def caculateSub(nums,s,n):
            if s == 0:
                return True
            if nums == []:
                return 0
            result_temp = []
            for i in range(len(nums)-1,-1,-1):
                temp = []
                if s == nums[i]:
                    temp.append(s)
                if nums[i] < s:
                    nums_candidate = []
                    for ii in range(len(nums)):
                        if nums[ii]>s-nums[i]:
                            break
                        nums_candidate.append(nums[ii])
                    n+=1
                    flag = caculateSub(nums_candidate,s-nums[i],n)
                    n-=1
                    if flag:
                        # try:
                        temp = [nums[i]] + flag[0]
                        # except KeyError:
                        #     temp = temp + [nums[i]
                if temp != [] and not n:
                    result_temp.append(temp)
                if temp != [] and n:
                    result_temp = temp
                # else:
                #     n = max(n-1,0)
            return [result_temp]   
        
        result = caculateSub(candidates,target,0)
        result = [sorted(seq) for seq in result[0]]
        result_tem = result
        for i in range(len(result)):
            for j in range(i+1,len(result)):
                if result[i] == result[j]:
                    result.remove(result[j])
        return sorted(result)

a = Solution()
candidates = [1,2]
target = 4
answer = a.combinationSum(candidates,target)
print(answer)
```

自己写的只能通过20个案例

```python
class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx > len(candidates)-1 or res <= 0:
                if res == 0:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res - candidates[idx]) 
            temp.pop()
            recursion(idx + 1, res)
        recursion(0, target)
        return ans 
```

正确答案,很漂亮简洁

## 42.接雨水
一次成功,成功经验:先写好思路再敲代码,效率高很多.在写while和if条件句的时候,把条件可能出现的情况集合考虑清楚,这样边界条件更清楚.

## 45.跳跃游戏 II

==难度Hard==

使用回溯方法,对任务进行切分,通过了73/92个案例,超时.

正确答案:

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step
```

