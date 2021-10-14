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

    def append(self, value) -> None:
        newNode: Node = Node(value)
        self.tail.next = newNode
        self.tail = newNode

    def print(self) -> None:
        tmp: 'Node' = self.head
        while True:
            print(tmp.value)
            if tmp == self.tail:
                break
            tmp = tmp.next

    def len(self) -> int:
        i: int = 1
        tmp: Node = self.head
        while tmp != self.tail
            i += 1
            tmp = tmp.next
        return i


    def node(self, at: int) -> Node:
        result: Node = self.head
        i: int = 1
        if at <= self.len():
            while i != at:
                i +=1
            return result
        else:
            print("Index out of bounds, LinkedList.len() is " self.len()+ "")

ll: LinkedList = LinkedList(2137)
ll.push(420)
ll.append(69)
ll.print()
