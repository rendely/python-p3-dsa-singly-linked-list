class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node 

    def __repr__(self):
        return f'Node(data={self.data})'

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def append(self, node):
        if self.head is None:
            self.head = node 
            return 

        last_node = self.head 
        while last_node.next_node:
            last_node = last_node.next_node
        
        last_node.next_node = node 

    def __repr__(self):
        return f'LinkedList(head={self.head})'