from tkinter.messagebox import NO


class Queue:

    def __init__(self, capacity) -> None:
        self.queue = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def isFull(self) -> None:
        return self.size == self.capacity

    def enqueue(self, value) -> None:
        if self.isFull():
            raise Exception("The Queue is full")
        self.queue[self.tail] = value
        # Implementing circular queue
        self.tail = (self.tail +1) % self.capacity
        self.size += 1

    def dequeue(self) -> None:
        if self.size == 0:
            raise Exception ("The Queue is empty")
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return data