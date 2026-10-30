class Queue:
    def __init__(self, capacity):
        # creates a list of none value slots with specified capacity
        self.internal_array = [None] * capacity
        self.front = 0
        # next available index in the list is rear
        self.rear = -1
        self.size = 0

        def add(self, item):
            if self.size == capacity:
                raise IndexError('Queue is full')

            self.rear = (self.rear + 1) % capacity

            self.internal_array[self.rear] = item

            self.length += 1
            pass

        def remove(self):
            if self.length == 0:
                raise IndexError('Queue is empty')

            item = self.internal_array[self.front]

            self.internal_array[self.front] = None

            self.front = (self.front + 1) % capacity

            self.size -= 1

            return item

