class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

class CircularLinkedList:
    def __init__(self):
        self.head = None
    def traverse(self,starting_node=None):
        if starting_node is None:
            starting_node = self.head
        node = starting_node
        while node is not None and node.next is not starting_node:
            yield node
            node = node.next
        yield node
    def print_list(self,starting_node=None):
        nodes = []
        for node in self.traverse(starting_node):
            nodes.append(str(node.data))
        print(' '.join(nodes))

