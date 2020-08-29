class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring = []
        self.oldest_node = 0

    def append(self, item):
        if len(self.ring) < self.capacity:
            self.ring.append(item)
        else:
            self.ring[self.oldest_node] = item
            self.oldest_node += 1
        # print(self.oldest_node)
        # 1 % 3 = 1 oldest = 0 + 1
        # 2 % 3 = 2 oldest = 1 + 1
        # 3 % 3 = 0 oldest = 2 + 1

    def get(self):
        return [item for item in self.ring]


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print(buffer.get())    # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print(buffer.get())    # should return ['d', 'e', 'f']
