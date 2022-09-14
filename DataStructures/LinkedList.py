class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self._head = None

    def addNode(self, value) -> None:
        if self._head is None:
            self._head = Node(value)
            return
        head = self._head
        while head.next:
            head = head.next
        head.next = Node(value)
        return

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, head: Node) -> None:
        if isinstance(head, Node):
            self._head = head
        else:
            self._head = Node(head)

    def __str__(self) -> None:
        print("Linked List:")
        head = self._head
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
