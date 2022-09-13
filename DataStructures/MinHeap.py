class MinHeap:

    def __init__(self, capacity) -> None:
        self.heap = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1)//2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2*index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        return self.heap[self.getParentIndex(index)]

    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, data):
        if(self.isFull()):
            raise("Heap is Full")
        self.heap[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)

    def heapifyUp(self, index):
        if (self.hasParent(index) and self.parent(index) > self.heap[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMin(self):
        if (self.size == 0):
            raise ("Empty Heap")
        data = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data

    def heapifyDown(self, index=0):
        while (self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.getRightChildIndex(index)
            if self.heap[index] < self.heap[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)
            index = smallerChildIndex

    def printHeap(self):
        for val in self.heap:
            print(val)


if __name__ == "__main__":

    unsorted_list = [10, 20, 5, 8, 0]
    minheap = MinHeap(len(unsorted_list))
    for val in unsorted_list:
        minheap.insert(val)
    minheap.printHeap()
