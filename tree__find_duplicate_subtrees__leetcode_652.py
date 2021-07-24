# https://leetcode.com/problems/find-duplicate-subtrees/
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of any one of them.
#
# Two trees are duplicate if they have the same structure with the same node values.
#
# examples:
#
# Input: root = [1, 2, 3, 4, null, 2, 4, null, null, 4]
# Output: [[2, 4], [4]]
#
# Input: root = [2,1,1]
# Output: [[1]]
#
# Input: root = [2,1,1]
# Output: [[1]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        visited = set()
        recorded = set()
        snode = []

        def helper(node):
            if node is None:
                return '#'
            s = str(node.val) + ' ' + helper(node.left) + ' ' + helper(node.right)
            s = s.strip()
            if s in visited and s not in recorded:
                snode.append(node)
                recorded.add(s)
            else:
                visited.add(s)
            return s

        helper(root)
        return snode
