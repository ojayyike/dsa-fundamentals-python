class CircularQueue:
    def __init__(self,capacity):
        self.q = [None] * capacity
        self.capacity = capacity
        self.count = 0
        self.front = 0
        self.rear = 0
    def enqueue(self,item):
        if self.is_full():
            raise IndexError("Queue is full")
        else:
            self.q[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.count += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Pop from empty queue")
        item = self.q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("Peep from empty queue")
        return self.q[self.front]
    def is_empty(self):
        return self.count == 0
    def is_full(self):
        return self.count == self.capacity
