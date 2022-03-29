from Lab02.LinkedList import LinkedList
from Lab02.Node import Node
from typing import Any, Callable


class Queue:
    def peek(self) -> Any:
        return self.storage.head.value

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)

    def dequeue(self) -> Any:
        return self.storage.pop()

    def run(self, foo: Callable[['Any'], None]):
        while len(self) != 0:
            foo(self.dequeue())

    def __init__(self):
        self.storage = LinkedList()

    def __len__(self) -> int:
        return len(self.storage)

    def __str__(self) -> str:

        if len(self) != 0:
            result: str = str(self.storage.head.value)

            if len(self) != 1:
                result += ", "
                nxt: Node = self.storage.head
                while nxt.next != self.storage.tail:
                    nxt = nxt.next
                    result += str(nxt.value) + ", "
                result += str(self.storage.tail.value)
            return result
        return ""
