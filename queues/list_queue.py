class QueueList:
    def __init__(self):
        self.q = []
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Pop from empty queue")
        item = self.q.pop(0)
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.q[0]
    def is_empty(self):
        return len(self.q) == 0
    def __str__(self):
        ret = ''
        for item in self.q:
            ret += str(item) + ' '
        return ret

q = QueueList()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  # Should be 10
print(q.peek())     # Should be 20
print(q.dequeue())  # Should be 20
print(q)    
