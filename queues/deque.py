from collections import deque
class QueueList:
    def __init__(self):
        self.q = deque()
    def enqueue(self,item):
        self.q.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        return self.q.popleft()
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty list")
        return self.q[0]
    def is_empty(self):
        return len(self.q) == 0
    def __str__(self):
        ret = ''
        for item in self.q:
            ret += str(item) + ' '
        return ret
d = QueueList()
d.append(10)      # Add to right - O(1)
d.appendleft(5)   # Add to left - O(1)
d.pop()           # Remove from right - O(1)
d.popleft()       # Remove from left - O(1)
