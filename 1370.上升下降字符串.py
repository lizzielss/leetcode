import collections
class Solution:
    def sortString(self, s: str) -> str:
        if s == '':
            return ''
        s = sorted(s)
        count = collections.OrderedDict()
        current = ''
        idx = 0
        while idx < len(s):
            if s[idx] != current:
                count[s[idx]] = 1
                current = s[idx]
            else:
                count[s[idx]] += 1
            idx += 1
        result = ''
        while max(count.values()):
            temp = ''
            for key in count.keys():
                if count[key] == 0:
                    continue
                else:
                    result += key
                    count[key] -= 1
                    if count[key] == 0:
                        continue
                    else:
                        temp += key
                        count[key] -= 1
            result += temp[::-1]
        return result

a = Solution()
s = "aaaabbbbcccc"
result = a.sortString(s)
print(result)