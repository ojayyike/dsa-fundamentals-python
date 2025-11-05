class Stack:
    def __init__(self,capacity=10):
        self.stack = [0] * capacity
        self.len = 0
        self.capacity = capacity

    def push(self,item):
        if self.len < self.capacity:
            self.stack[self.len] = item
            self.len += 1
        else:
            temp = [0] * self.capacity * 2
            self.capacity *= 2
            for idx,value in enumerate(self.stack):
                temp[idx] = value 
            self.stack = temp
            self.stack[self.len] = item
            self.len += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        self.len -= 1
        item = self.stack[self.len]
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek from empty stack")
        return self.stack[self.len - 1]
    
    def is_empty(self):
        return self.len == 0

    def is_full(self):
        return self.len == self.capacity

s = Stack(capacity=2)
s.push(10)
s.push(20)
s.push(30)  # Triggers resize
print(f"Top: {s.peek()}")  # Should print 30
print(f"Pop: {s.pop()}")   # Should print 30
print(f"Pop: {s.pop()}")   # Should print 20
print(f"Pop: {s.pop()}")   # Should print 10
print(f"Pop: {s.pop()}")   # Should raise IndexError
