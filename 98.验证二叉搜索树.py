#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def subfunction(root, lower=float('-inf'), upper=float('inf')):
            if root == None:
                return True
            if root.val > lower and root.val < upper:
                return subfunction(root.left, lower, root.val) and subfunction(root.right, root.val, upper)
            else:
                return False
        return subfunction(root)
# @lc code=end

