from dataclasses import dataclass


class Node: 

    def __init__(self, data, left=None, right=None) -> None:
        self.value = data 
        self.left = left 
        self.right = right 


class BST:

    def __init__(self) -> None:
        self.root = None