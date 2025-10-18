class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.tail = self.head
    def insert_head(self,data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head
    def insert_tail(self,data):
        if not self.tail:
            self.tail = Node(data)
            self.head = self.tail
        else:
            new_tail = Node(data)
            self.tail.next = new_tail
            self.tail = new_tail
    def remove(self,data):
        if not self.head:
            return
        if data == self.head.value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        current = self.head
        while current.next and current.next.value != data:
            current = current.next
        if not current.next:
            return
        current.next = current.next.next
        if not current.next:
            self.tail = current 
    def search(self,data):
        current = self.head
        while current:
            if current.value == data:
                return True
            current = current.next
        return False
    
ll = LinkedList()
ll.insert_tail(1)
ll.insert_tail(2)
ll.insert_tail(3)
ll.remove(1)  # Remove head
ll.remove(3)  # Remove tail
ll.remove(2)  # Remove last node
print(ll.head)  # Should be None
print(ll.tail)  # Should be None
