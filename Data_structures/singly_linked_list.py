class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Time Complexity:  
        add element to list O(1)
        remove element from list O(1)
        search for value in list O(n)
    """
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
        for data in nodes:
            node.next = Node(data)
            node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
 
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' '.join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node