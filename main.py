from Lab02.LinkedList import LinkedList

list_ = LinkedList()
assert list_.head is None

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
