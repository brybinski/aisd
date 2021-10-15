from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value: Any = value

    next: 'Node'


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
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

            return(result)
        else:
            return("None")

    def __len__(self) -> int:
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


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'



first_element = list_.node(at=0)
returned_first_element = list_.pop()
print(list_)
assert first_element.value == returned_first_element


last_element = list_.node(at=3)
print(last_element.value)
returned_last_element = list_.remove_last()
print(returned_last_element)
assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'



second_node = list_.node(at=1)
print(list_)
list_.remove(second_node)
assert str(list_) == '1 -> 5'


