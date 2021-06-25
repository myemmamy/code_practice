# https://leetcode.com/problems/construct-string-from-binary-tree/
# Given the root of a binary tree, construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
# Example 1:
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originallay it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
#
# Example 2:
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def helper(node):
            s = ''
            if node is None:
                return
            #return f'{node.val}({helper(node.left)})({helper(node.right)})'
            s += str(node.val)
            has_left=False
            if node.left:
                s += '('+helper(node.left)+')'
                has_left=True
            if node.right:
                if not has_left:
                    s += '()' # add empty () if there's miss left but has right
                s += '('+helper(node.right)+')'
            return s
        return helper(root)