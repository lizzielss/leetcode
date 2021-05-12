#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        per = 2 * numRows - 2
        row = numRows
        if len(s) % per == 0:
            col = (numRows - 1) * (len(s) // per)
        else:
            col = (numRows - 1) * (len(s) // per + 1)
        # col = 
        metrix = [['' for j in range(col)] for i in range(row)]
        r, c = 0, 0
        idx = 0
        direction = 'down'
        while True:
            if idx == len(s):
                break
            if direction == 'down':
                metrix[r][c] = s[idx]
                idx += 1
                if r == row - 1:
                    r -= 1
                    c += 1
                    direction = 'up'
                    continue
                else:
                    r += 1
            if direction == 'up':
                metrix[r][c] = s[idx]
                idx += 1
                if r == 0:
                    r += 1
                    direction = 'down'
                else:
                    r -= 1
                    c += 1
        result = ''
        for row in metrix:
            temp = ''.join(row)
            result += temp
        return result
            
# a = Solution()
# s = "ABCDE"
# result = a.convert(s,4)
# print(result)
# @lc code=end

