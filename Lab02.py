from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value: Any = value

    next: 'Node'


class LinkedList:
    def __init__(self, value: Any) -> None:
        self.head: Node = Node(value)
        self.tail: Node = self.head

    def push(self, value: Any) -> None:
        newNode: Node = Node(value)
        newNode.next = self.head
        self.head = newNode
        if self.tail is None:
            self.tail = newNode

    def append(self, value) -> None:
        newNode: Node = Node(value)
        self.tail.next = newNode
        self.tail = newNode

    def print(self) -> None:
        if self.head is not None:
            result: str = str(self.head.value)
            if self.head.next is None:
                print(result)
                return
            else:
                tmp: 'Node' = self.head
                while tmp.next is not self.tail:
                    tmp = tmp.next
                    result += "->" + str(tmp.value)
            print(result)
        else:
            print("None")

    def len(self) -> int:
        i: int = 1
        if self.head is None:
            return 0

        tmp: Node = self.head
        while tmp != self.tail:
            i += 1
            tmp = tmp.next
        return i

    def insert(self, value: Any, after: Node) -> None:
        tmp = after.next
        after.next = Node(value)
        after.next.next = tmp

    def node(self, at: int) -> Node:
        result: Node = self.head
        i: int = 1
        if at <= self.len():
            while i != at:
                result = result.next
                i += 1
            return result
        else:
            print(f"Index out of bounds, LinkedList.len() is {self.len()} but {at} was given")

    def pop(self) -> Any:
        result: int = self.head
        if self.head != self.tail:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        return result


ll: LinkedList = LinkedList(2137)
ll.push(420)
ll.append(69)
ll.insert("xD", ll.node(2))
ll.print()
print(ll.node(2).value)
ll.pop()
ll.pop()
ll.pop()
ll.pop()
print(ll.len())
ll.print()
ll.push(911)
ll.print()
