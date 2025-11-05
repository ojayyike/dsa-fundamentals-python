class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    def push(self,item):
        if not self.head:
            self.head = Node(item)
        else:
            new_head = Node(item)
            new_head.next = self.head
            self.head = new_head

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.head
        self.head = self.head.next
        return item.value
    def peek(self):
        if self.is_empty():
            raise IndexError ("List is empty")
        return self.head.value
    def is_empty(self):
        return not self.head
    
    def __str__(self):
        curr = self.head
        ret = ''
        while curr.next:
            ret += str(curr.value) + ' -> '
            curr = curr.next
        if curr:
            ret += str(curr.value)
        return ret

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
s.pop()
print(s.peek())
print(s)
s.pop()
print(s.peek())
print(s)

