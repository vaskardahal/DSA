# Source: https://www.youtube.com/watch?v=8wQbIOdbfCk&ab_channel=NoobCoder

class Node: 

    def __init__(self, data, left=None, right=None) -> None:
        self.value = data 
        self.left = left 
        self.right = right 
    
    def insert(self, data) -> None:
        if(self.data == data):
            raise Exception("Data already exists within the tree")
        elif (self.data > data):
            if (self.left):
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if (self.right):
                self.right.insert(data)
            else:
                self.right = Node(data)
    
    def delete(self, data) -> None: 
        if (data < self.data and self.left):
            self.left = self.left.delete(data)
        elif(data > self.data and self.right):
            self.right = self.right.delete(data)
        else:
            if (self.data == data):
                if (self.right and self.left):
                    minVal = self.right.findMin()
                    self.data = minVal
                    self.right = self.right.delete(minVal)
                elif(self.left):
                    return self.left
                elif(self.right):
                    return self.right
                else:
                    return None 
        return self

    def findMin(self):
        if (self.left):
            return self.left.findMin()
        else:
            return self.data

    def find(self, data):
        if self is None:
            return False
        if (self.data == data):
            return True
        elif (self.data > data):
            return self.left.find(data)
        else:
            return self.right.find(data)




class BST:

    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        if (self.root):
            self.root.insert(data)
        else:
            self.root = Node(data)

    
    def delete(self, data) -> None:
        if (self.root):
            self.root = self.root.delete(data)


    def find(self, data) -> bool: 
        if (self.root):
            return self.root.find(data)


