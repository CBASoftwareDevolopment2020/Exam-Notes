from utils import Node


class ArrayStack:
    def __init__(self):
        self._items = []
        self._size = 0

    def push(self, item):
        self._items.append(item)
        self._size += 1

    def pop(self):
        item = self._items.pop()
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def __iter__(self):
        yield from self._items[:self._size]


class LinkedStack:
    def __init__(self):
        self._last = None
        self._size = 0
        self._next = None

    def push(self, item):
        self._last = Node(item, self._last)
        self._size += 1

    def pop(self):
        item, self._last = self._last.item, self._last.next
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def __iter__(self):
        self._next = self._last
        return self

    def __next__(self):
        if self._next is None:
            raise StopIteration
        item, self._next = self._next.item, self._next.next
        return item
