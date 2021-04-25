class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        temp = []
        def recursion(idx, res):
            if idx < 0 or res <= 0:
                if res == 0:
                    ans.append(temp[:])
                return
            temp.append(candidates[idx])
            recursion(idx, res - candidates[idx]) 
            temp.pop()
            recursion(idx - 1, res)
        recursion(len(candidates)-1, target)
        return ans 
a = Solution()
candidates = [2,3,6,7]
target = 7
answer = a.combinationSum(candidates,target)
print(answer)