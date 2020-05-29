from utils import Node


class ArrayQueue:
    def __init__(self):
        self._items = []
        self._size = 0

    def enqueue(self, item):
        self._items.append(item)
        self._size += 1

    def dequeue(self):
        item = self._items.pop(0)
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def __iter__(self):
        yield from self._items[:self._size]


class LinkedQueue:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0
        self._next = None

    def enqueue(self, item):
        if self._last:
            new = Node(item, None, self._last)
            self._last.next, self._last = new, new
        else:
            self._first = self._last = Node(item)
        self._size += 1

    def dequeue(self):
        item, self._first = self._first.item, self._first.next
        if self._first is None:
            self._last = None
        self._size -= 1
        return item

    def is_empty(self):
        return self._size == 0

    def get_size(self):
        return self._size

    def __iter__(self):
        self._next = self._first
        return self

    def __next__(self):
        if self._next is None:
            raise StopIteration
        item, self._next = self._next.item, self._next.next
        return item
