class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'Node({self.data})'

# class LinkedList:
    # def __init__(self,nodes=None):
        #     self.head = None
        #     if nodes:
        #         self.head = Node(nodes.pop(0))
        #     node = self.head
        #     for i in range(len(nodes)):
        #         node.next = Node(nodes[i])
        #         node = node.next

    # def __iter__(self):
    #     return self
    # def __next__(self):
    #     if self.current is not None:
    #         node = self.current
    #         self.current = self.current.next
    #         return node
    #     else:
    #         raise StopIteration()


class LL:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None and len(nodes)>0:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join([str(v) for v in nodes])
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def insertleft(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
    def remove(self,data):
        if self.head is None:
            raise Exception('List is empty')
        if self.head.data == data:
            self.head = self.head.next
            return self
        node = self.head
        nnode = node.next
        while nnode is not None:
            if nnode.data == data:
                node.next = nnode.next
                return self
            node = nnode
            nnode = nnode.next
        raise Exception(f'Not find a node with {data} in the list')









