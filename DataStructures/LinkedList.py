class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def addNode(self, value) -> None:
        if self.head is None:
            self.head = Node(value)
            return
        head = self.head
        while head.next:
            head = head.next
        head.next = Node(value)
        return

    def __str__(self) -> None:
        print("Linked List:")
        head = self.head
        while head:
            print(f"{head.val}", end="")
            head = head.next
            if head:
                print(f" -> ", end="")
        return "\n"


if __name__ == '__main__':
    values = [2, 7, 3, 4, 2]
    ll = LinkedList()
    for val in values:
        ll.addNode(val)
    print(ll)
