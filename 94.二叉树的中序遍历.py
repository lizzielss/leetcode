#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (75.28%)
# Likes:    930
# Dislikes: 0
# Total Accepted:    409.1K
# Total Submissions: 543.4K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
# 示例 4：
#
#
# 输入：root = [1,2]
# 输出：[2,1]
#
#
# 示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 100] 内
# -100
#
#
#
#
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
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
        self.path = []
    def inorderTraversal(self, root: TreeNode):
        if  root == None:
            return []
        temp_path = []
        temp_path += self.inorderTraversal(root.left)
        temp_path += [root.val]
        temp_path += self.inorderTraversal(root.right)
        return temp_path

# a = Solution()
# root = TreeNode(val=1,right=TreeNode(val=2,left=TreeNode(val=3)))
# result = a.inorderTraversal(root)
# print(result)
# @lc code=end

