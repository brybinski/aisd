from typing import Any
from Lab02.Node import Node


# noinspection SpellCheckingInspection,PyTypeChecker
class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = self.head

    def push(self, value: Any) -> None:
        newnd: Node = Node(value)
        newnd.next = self.head
        self.head = newnd
        if self.tail is None:
            self.tail = newnd

    def append(self, value) -> None:
        if len(self) == 0:
            self.push(value)
            return
        newnd: Node = Node(value)
        self.tail.next = newnd
        self.tail = newnd

    def __str__(self) -> str:
        if self.head is not None:
            result: str = str(self.head.value)
            if self.head.next is None:
                return result
            else:
                tmp: Node = self.head
                while tmp is not self.tail:
                    tmp = tmp.next
                    result += " -> " + str(tmp.value)

            return result
        else:
            return "None"

    def __len__(self) -> int:
        i: int = 1
        if self.head is None:
            return 0

        tmp: Node = self.head
        while tmp != self.tail:
            i += 1
            tmp = tmp.next
        return i

    # noinspection PyMethodMayBeStatic
    def insert(self, value: Any, after: Node) -> None:
        tmp = after.next
        after.next = Node(value)
        after.next.next = tmp

    def node(self, at: int) -> Node:
        result: Node = self.head
        i: int = 0
        if at <= len(self):
            while i != at:
                result = result.next
                i += 1
            return result
        else:
            raise ValueError(
                "Index out of bounds, LinkedList.len() is " + str(len(self)) + " but " + str(at) + " was given")

    def pop(self) -> Any:
        result: int = self.head.value
        if self.head != self.tail:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        return result

    def remove_last(self) -> Any:
        result: Any = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return result

        tmp: Node = self.head
        while tmp.next != self.tail:
            tmp = tmp.next
        self.tail = tmp

        return result

    def remove(self, after: Node):
        if after == self.tail:
            raise ValueError("Wrong node, index out of bound")
        if after.next == self.tail:
            self.tail = after
        else:
            after.next = after.next.next


