#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#
# https://leetcode-cn.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (43.03%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 73.2K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
#
# 注意：两个节点之间的路径长度由它们之间的边数表示。
#
# 示例 1:
#
# 输入:
#
#
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
#
#
# 输出:
#
#
# 2
#
#
# 示例 2:
#
# 输入:
#
#
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
#
#
# 输出:
#
#
# 2
#
#
# 注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans=0
        def find_row(node):
            if not node:
                return 0
            left_len=find_row(node.left)
            right_len=find_row(node.right)
            left_row=right_row=0
            if node.left and node.left.val==node.val:#判断左端点存在并且值相等
                left_row=left_len+1
            if node.right and node.right.val==node.val:
                right_row=right_len+1
            self.ans=max(self.ans,left_row+right_row)
            return max(left_row,right_row)
        find_row(root)
        return self.ans

    # def __init__(self):
    #     self.maxlength = 0
    # def subfunction(self, root: TreeNode) -> int:
    #     if root == None:
    #         return 0
    #     length_left = self.subfunction(root.left)
    #     length_right = self.subfunction(root.right)
    #     length = 0
    #     if root.left and root.right:
    #         if root.left.val == root.val and root.right.val == root.val:
    #             length = length_right + length_left + 2
    #         elif root.left.val == root.val:
    #             length = length_left + 1
    #         elif root.right.val == root.val:
    #             length = length_right + 1
    #     elif root.left and root.left.val == root.val:
    #         length = length_left + 1
    #     elif root.right and root.right.val == root.val:
    #         length = length_right + 1
    #     if length > self.maxlength:
    #         self.maxlength = length
    #     if root.val == root.left.val or root.val == root.right.val:
    #         return max(length_right,length_left) + 1
    #     else:
    #         return 0
        # else:
        #     if root.left.val ==  root.val:
        #         length = self.subfunction(root.left) + 1
        #     elif root.right.val == root.val:
        #         length = self.subfunction(root.right) + 1
        #     else:
        #         length = max(self.subfunction(root.left),self.subfunction(root.right))
        # return length
    # def longestUnivaluePath(self, root: TreeNode) -> int:
    #     self.subfunction(root)
    #     return self.maxlength

# a = Solution()
# root = TreeNode(val=1,left=TreeNode(val=4,left=TreeNode(val=4),right=TreeNode(val=4)),right=TreeNode(val=5,right=TreeNode(val=5)))
# result = a.longestUnivaluePath(root)
# print(result)
# @lc code=end

