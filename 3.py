# Created on Lizzie‘s iPad.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        result = []
        temp = ''
        while r < len(s):
            while r < len(s) and len(set(temp)) == len(temp):
                temp = temp + s[r]
                r += 1
            if r != len(s):    
                temp = list(temp).pop()
                temp = ''.join(temp)
                result.append([len(temp),temp])
                temp += s[r]
            else:
                result.append([len(temp),temp])
            while l <= r and len(set(temp)) != len(temp):
                l += 1
                temp = s[l:r+1]
        result = sorted(result,key=lambda x:x[0],reverse=True)
        print(result)
        return result[0][1]
# print ('Hello World!')
