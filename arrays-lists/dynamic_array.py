class DynamicArray:
    def __init__(self,capacity=2):
        self.len = 0
        self.capacity = capacity
        self.array = [None] * self.capacity
    def append(self,item):
        if self.len >= self.capacity:
            new_array = [None] * (self.capacity * 2)
            self.capacity *= 2
            for i in range(self.len):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[self.len] = item
        self.len += 1
    def get(self,idx):
        if idx < 0 or idx >= self.len:
            return 'Index oout of bounds'
        return self.array[idx]
    def set(self,item,idx):
        if idx < 0 or idx >= self.len:
            raise IndexError
        self.array[idx] = item
    def remove(self,idx):
        if idx < 0 or idx > self.len:
            raise IndexError
        self.array = self.array[:idx] + self.array[idx+1:]
        self.len -= 1
    def __len__(self):
        return self.len

arr = DynamicArray()
print(len(arr))  # Should be 0
arr.append(10)
arr.append(20)
arr.append(30)
print(len(arr))  # Should be 3
print(arr.get(0))  # Should be 10
arr.set(999, 1)
print(arr.get(1))  # Should be 999
arr.remove(1)
print(len(arr))  # Should be 2
print(arr.get(1))  # Should be 30
