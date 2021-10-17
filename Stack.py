from LinkedList import LinkedList
from Node import Node
from typing import Any


class Stack:

    def __init__(self):
        self.storage: LinkedList = LinkedList()

    def __len__(self) -> int:
        return len(self.storage)

    def push(self, element: Any) -> None:
        self.storage.append(element)

    def pop(self) -> Any:
        length: int = len(self.storage)
        if length != 0:
            result: Any = self.storage.tail.value
            if length > 1:
                self.storage.tail = self.storage.node(len(self.storage) - 2)
                return result

            self.storage.tail = None
            self.storage.head = None
            return result
        return None

    def __str__(self) -> str:

        if len(self) != 0:
            result: str = str(self.storage.head.value)
            nxt: Node = self.storage.head
            while nxt != self.storage.tail:
                nxt = nxt.next
                result = str(nxt.value) + "\n" + result
            return result
        return ""
