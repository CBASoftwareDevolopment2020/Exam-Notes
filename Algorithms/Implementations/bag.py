import unittest


class ArrayBag:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, item):
        self._items[self._size], self._size = item, self._size + 1

    def __iter__(self):
        yield from self._items[:self._size]

    def is_empty(self):
        return self._size == 0


class BagTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = ArrayBag(10)
        self.assertEqual(0, bag._size, msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = ArrayBag(10)
        bag.add(1)
        count = 0
        for item in iter(bag):
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag._size, msg=f'Bag should have {count} items')

    def test_add_full(self):
        capacity = 10
        bag = ArrayBag(capacity)
        for i in range(1):
            bag.add(i)
        self.assertRaises(IndexError, bag.add(10), msg=f'Bag can only hold {capacity} items')


if __name__ == "__main__":
    unittest.main()
