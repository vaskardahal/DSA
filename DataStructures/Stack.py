class Stack: 

    def __init__(self, size) -> None:
        self.stack = [None] * size
        self.top = -1 # For empty array

    def push(self, data) -> None:
        if (self.isFull()):
            raise Exception("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self) -> object:
        if (self.top == -1):
            return None
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data

    def getSize(self):
         return self.top + 1

    def peek(self) -> object:
        return self.storage[self.top]

    def isFull(self) -> bool:
        return self.getSize() == len(self.stack)
