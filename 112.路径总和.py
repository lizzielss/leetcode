#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (52.09%)
# Likes:    570
# Dislikes: 0
# Total Accepted:    198K
# Total Submissions: 380.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点
# 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
#
#
# 示例 3：
#
#
# 输入：root = [1,2], targetSum = 0
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [0, 5000] 内
# -1000
# -1000
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
        # self.sum = 0
        self.flag = False
    def hasPathSum(self, root: TreeNode, targetSum: int):
        if root == None:
            return False
        if self.flag:
            return True
        if targetSum == root.val:
            if root.left== None and root.right == None:
                self.flag = True
        targetSum -= root.val
        if root.left:
            self.hasPathSum(root.left,targetSum)
        if root.right:
            self.hasPathSum(root.right,targetSum)
        return self.flag


# a = Solution()
# targetSum = 22
# root = TreeNode(val=5, left=TreeNode(val=4,left=TreeNode(val=11,left=TreeNode(val=7),right=TreeNode(val=2))),right=TreeNode(val=8,left=TreeNode(val=13),right=TreeNode(val=4,right=TreeNode(val=1))))
# result = a.hasPathSum(root,targetSum)
# print(result)
# @lc code=end

