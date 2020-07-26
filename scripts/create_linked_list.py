__author__ = '[Kamil Adamski](https://github.com/adamsqi)'
__date__ = '2020.07.26'

"""
This program creates a linked list and prints the total number of nodes.

Program:
```python
example_elements = [1, 3, 6, 2, 1, 5]
linked_list = LinkedList(example_elements)
linked_list.create()
linked_list.count_number_of_nodes(linked_list.nodes[0])
```

Results:
```python
Total number of nodes equals to: 6
```
"""

from typing import List


class Node:
    next = None

    def __init__(self, data: int):
        self.data = data


class LinkedList:
    def __init__(self, elements: List[int]):
        self.elements = elements
        self.nodes = []
        self.counter = 0

    def create(self) -> None:
        for el in self.elements:
            node = Node(el)
            self.nodes.append(node)
        self._connect_nodes()

    def _connect_nodes(self) -> None:
        for i, node in enumerate(self.nodes[:-1]):
            node.next = self.nodes[i + 1]

    def count_number_of_nodes(self, head: Node) -> None:
        self.counter += 1
        if head.next is not None:
            self.count_number_of_nodes(head.next)


def main():
    example_elements = [1, 3, 6, 2, 1, 5]
    linked_list = LinkedList(example_elements)
    linked_list.create()
    linked_list.count_number_of_nodes(linked_list.nodes[0])
    print(f'Total number of nodes equals to: {linked_list.counter}')


if __name__ == '__main__':
    main()
