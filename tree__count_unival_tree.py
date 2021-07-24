# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

################
#solution link
##https://www.dailycodingproblem.com/solution/8?token=3de3047997d2db161880a63c9ab49bcd910223784623345e8e568497c163480b5fb263bc
#   a
#  / \
# a   a
#     /\
#    a  a
#        \
#         A
# This tree has 3 unival subtrees: the two 'a' leaves, and the one 'A' leaf. The 'A' leaf causes all its parents to not be counted as a unival tree.
#
#   a
#  / \
# c   b
#     /\
#    b  b
#         \
#          b
# This tree has 5 unival subtrees: the leaf at 'c', and every 'b'.
# We can start off by first writing a function that checks whether a tree is unival or not. Then, perhaps we could use this to count up all the nodes in the tree.
#
# To check whether a tree is a unival tree, we must check that every node in the tree has the same value. To start off,
# we could define an is_unival function that takes in a root to a tree. We would do this recursively with a helper function.
# Recall that a leaf qualifies as a unival tree.



class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def checkUniversal(node,val):
    if node is None:
        return True
    if node.val != val:
        return False
    result = False
    if node.left:
        result = result and checkUniversal(node.left,node.val)
    if node.right:
        result = result and checkUniversal(node.right,node.val)
    return result

def isUniversalTree(root):
    checkUniversal(root,root.val)

def countUniversalTree(root):
    if root is None:
        return 0
    num = 0
    num1 = countUniversalTree(root.left)
    num2 = countUniversalTree(root.right)
    if isUniversalTree(root):
        return num1 + num2 + 1
    else:
        return num1 + num2







