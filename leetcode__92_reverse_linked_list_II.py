# https://leetcode.com/problems/reverse-linked-list-ii/
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
#
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
#
# Input: head = [5], left = 1, right = 1
# Output: [5]
#
# Constraints:
#
# The number of nodes in the list is n.
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        pos = 1
        prev = None
        node = head
        while pos < left:
            prev = node
            node = node.next
            pos += 1
        lnodeprev = prev
        lnode = node

        prev = None

        while pos < right:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            tmp = tmp.next
            pos += 1

        rnode = node
        rnodenext = rnode.next
        node.next = prev

        lnode.next = rnodenext
        if lnodeprev:
            lnodeprev.next = rnode
            return head
        else:
            return rnode






