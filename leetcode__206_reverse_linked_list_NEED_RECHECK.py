# https://leetcode.com/problems/reverse-linked-list/

class Solution(object):
    def reverseList(self, head):
        if head is None:
            return None
        prev = None
        node = head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev