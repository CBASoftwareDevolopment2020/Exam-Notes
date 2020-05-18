import unittest

from bag import ArrayBag, LinkedBag
from queue import ArrayQueue, LinkedQueue
from utils import Node


class NodeTest(unittest.TestCase):
    def test_node_item(self):
        value = 0
        node = Node(value)
        self.assertEqual(value, node.item, msg=f'Node item should be {value}')

    def test_node_prev(self):
        value = 0
        prev = Node(value)
        node = Node(8, prev=prev)

        self.assertEqual(value, node.prev.item, msg=f'Node prev item should be {value}')

    def next(self):
        value = 0
        next = Node(value)
        node = Node(8, next)

        self.assertEqual(value, node.next.item, msg=f'Node next item should be {value}')


class ArrayBagTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = ArrayBag(10)
        self.assertEqual(0, bag.get_size(), msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = ArrayBag(10)
        for i in range(10):
            bag.add(i)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag.get_size(), msg=f'Bag should have {count} items')
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
        self.assertEqual(0, bag.get_size(), msg='Bag should be empty')
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
        self.assertEqual(count, bag.get_size(), msg=f'Bag should have {count} items')
        for e, a in zip([i for i in lst[::-1]], list(bag)):
            self.assertEqual(e, a, msg='Should be equal')


class ArrayQueueTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = ArrayQueue()
        self.assertEqual(0, bag.get_size(), msg='Queue should be empty')
        self.assertTrue(bag.is_empty(), msg='Queue should be empty')

    def test_dequeue_empty(self):
        bag = ArrayQueue()
        with self.assertRaises(IndexError):
            bag.dequeue()

    def test_enqueue(self):
        bag = ArrayQueue()
        lst = range(10)
        for i in lst:
            bag.enqueue(i)
        count = 0
        for i, item in enumerate(bag):
            count += 1
            self.assertEqual(lst[i], item, msg='Items should be in the right order')
        self.assertEqual(len(lst), bag.get_size(), msg=f'Queue should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Queue should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(bag), msg='All items added to the Queue should be in the Queue')

    def test_dequeue(self):
        bag = ArrayQueue()
        lst = range(10)
        for i in lst:
            bag.enqueue(i)
        for e in lst:
            self.assertEqual(e, bag.dequeue(), msg='Items should be in the right order')


class LinkedQueueTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = LinkedQueue()
        self.assertEqual(0, bag.get_size(), msg='Queue should be empty')
        self.assertTrue(bag.is_empty(), msg='Queue should be empty')

    def test_enqueue(self):
        bag = LinkedQueue()
        lst = range(10)
        for i in lst:
            bag.enqueue(i)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        for e, a in zip(lst, list(bag)):
            self.assertEqual(e, a, msg='Should be equal')
        self.assertEqual(len(lst), bag.get_size(), msg=f'Queue should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Queue should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(bag), msg='All items added to the Queue should be in the Queue')

    def test_dequeue(self):
        bag = LinkedQueue()
        lst = range(10)
        for i in lst:
            bag.enqueue(i)
        for e in lst:
            self.assertEqual(e, bag.dequeue(), msg='Items should be in the right order')

    def test_dequeue_empty(self):
        bag = LinkedQueue()
        with self.assertRaises(AttributeError):
            bag.dequeue()


if __name__ == "__main__":
    unittest.main()
