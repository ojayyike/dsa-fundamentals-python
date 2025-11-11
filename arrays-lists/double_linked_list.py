class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self,data):
        new_head = Node(data)
        if not self.head:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

    def insert_tail(self,data):
        new_tail = Node(data)
        if not self.tail:
            self.tail = new_tail
            self.head = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail
    
    def delete(self,data):
        curr = self.head
        while curr and curr.value != data:
            curr = curr.next
        if not curr:
            return
        if curr == self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif curr == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            next_node = curr.next
            curr.prev.next = next_node
            next_node.prev = curr.prev

    def reverse_traversal(self):
        curr = self.tail
        while curr:
            print(str(curr.value))
            curr = curr.prev

    def __str__(self):
        curr = self.head
        ret = ''
        while curr:
            ret += str(curr.value)
            if curr.next:
                ret += '<->'
            curr = curr.next
        return ret
        
