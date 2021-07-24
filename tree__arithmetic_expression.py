# https://www.dailycodingproblem.com/solution/50?token=c507dac88da90507c53d019ae3d68810ec9b5696ca423dea0052b22706d702e631d1cc8f
# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).

def getExpression(root):
    def helper(node):
        s = ''
        if node is None:
            return ''
        s += '(' + str(node.val) + ')'
        s += helper(node.left)
        s += helper(node.right)
        return s
    s = eval(helper(root))
    return s

def calculate(root):
    def helper(node):
        if node is None:
            return 0
        if node.val == '*':
            num = node.left * node.right
        elif node.val == '+':
            num = node.left + node.right
        elif node.val == '/':
            num = node.left / node.right
        else:
            num = node.left - node.right
        return num
    if root is not None:







