#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.22%)
# Likes:    851
# Dislikes: 0
# Total Accepted:    296.2K
# Total Submissions: 461.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# 返回其层序遍历结果：
#
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
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
    def __init__(self):
        self.root_flag = True
    def levelOrder(self, root: TreeNode):
        ans, level = [],[root]
        while root and level:
            ans.append([node.val for node in level])
            LRpairs = [(node.left,node.right) for node in level]
            level = []
            for pair in LRpairs:
                for node in pair:
                    if node:
                        level.append(node)
        return ans
# a= Solution()
# root = TreeNode(val=3,left=TreeNode(val=9),right=TreeNode(val=20,left=TreeNode(val=15),right=TreeNode(val=7)))
# result = a.levelOrder(root)
# print(root)
# @lc code=end

