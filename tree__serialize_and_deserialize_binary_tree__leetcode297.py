# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
#
# Input: root = []
# Output: []
# Example 3:
#
# Input: root = [1]
# Output: [1]
# Example 4:
#
# Input: root = [1,2]
# Output: [1,2]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#180ms run time, 19.1MB memory
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        q = []
        nodes = []
        if root == None:
            return ''

        q.append(root)
        while q:
            node = q.pop(0)
            if node is None:
                nodes.append('None')
            else:
                nodes.append(str(node.val))
                if node.left is not None:
                    q.append(node.left)
                else:
                    q.append(None)
                if node.right is not None:
                    q.append(node.right)
                else:
                    q.append(None)
        s s= ' '.join(nodes)
        return ss


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        ldata = data.split()
        parent q =[]
        roo t =None

        while ldata:
            if root is None:
                val = ldata.pop(0)
                root = TreeNode((val))
                parentq.append(root)
            parentnode = parentq.pop(0)
            left = ldata.pop(0)
            right = ldata.pop(0)
            if left != 'None':
                parentnode.left = TreeNode((left))
                parentq.append(parentnode.left)
            if right != 'None':
                parentnode.right = TreeNode((right))
                parentq.append(parentnode.right)
        return root