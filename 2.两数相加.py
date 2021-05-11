#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        while l1.next != None:
            s1 += str(l1.val)
            l1 = l1.next
        s1 += str(l1.val)
        s2 = ''
        while l2.next != None:
            s2 += str(l2.val)
            l2 = l2.next
        s2 += str(l2.val)
        s = str(int(s1[::-1]) + int(s2[::-1]))
        # s = s[::-1]
        out = ListNode(val=int(s[0]),next=None)
        for i in range(1, len(s)):
            out = ListNode(val=int(s[i]), next=out)
        return out

# @lc code=end
