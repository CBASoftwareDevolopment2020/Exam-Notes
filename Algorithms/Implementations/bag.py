import numpy as np
import unittest


class ArrayBag:
    def __init__(self, capacity):
        self._items = np.zeros(capacity)
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, item):
        self._items[self._size], self._size = item, self._size + 1

    def __iter__(self):
        yield from self._items[:self._size]

    def is_empty(self):
        return self._size == 0


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return self.item == other.item


class LinkedBag:
    def __init__(self):
        self._first = None
        self._next = None
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, item):
        self._first = Node(item, self._first)
        self._size += 1

    def __iter__(self):
        self._next = self._first
        return self

    def __next__(self):
        if self._next is None:
            raise StopIteration
        item, self._next = self._next, self._next.next
        return item

    def is_empty(self):
        return self._size == 0


class ArrayBagTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = ArrayBag(10)
        self.assertEqual(0, bag._size, msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = ArrayBag(10)
        for i in range(10):
            bag.add(i)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag._size, msg=f'Bag should have {count} items')
        self.assertSequenceEqual(list(range(10)), list(bag), msg='All items added to the bag should be in the Bag')

    def test_add_full(self):
        capacity = 10
        bag = ArrayBag(capacity)
        for i in range(10):
            bag.add(i)
        with self.assertRaises(IndexError):
            bag.add(10)


class LinkedBagTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = LinkedBag()
        self.assertEqual(0, bag._size, msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = LinkedBag()
        lst = range(10)
        for i in lst:
            bag.add(i)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag._size, msg=f'Bag should have {count} items')
        for e, a in zip([Node(i) for i in lst[::-1]], list(bag)):
            self.assertEqual(e, a, msg='Should be equal')


if __name__ == "__main__":
    unittest.main()
