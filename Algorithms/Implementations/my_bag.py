import numpy as np

from utils import Node


class ArrayBag:
    def __init__(self, capacity):
        self._items = np.array([None] * capacity)
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, item):
        self._items[self._size], self._size = item, self._size + 1

    def __iter__(self):
        yield from self._items[:self._size]

    def is_empty(self):
        return self._size == 0


class LinkedBag:
    def __init__(self):
        self._first = None
        self._next = None
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, item):
        self._first, self._size = Node(item, self._first), self._size + 1

    def __iter__(self):
        self._next = self._first
        return self

    def __next__(self):
        if self._next is None:
            raise StopIteration
        item, self._next = self._next.item, self._next.next
        return item

    def is_empty(self):
        return self._size == 0
