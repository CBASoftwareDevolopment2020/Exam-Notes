import unittest

from bag import ArrayBag, LinkedBag
from queue import ArrayQueue, LinkedQueue
from stack import ArrayStack, LinkedStack
from utils import Node


class NodeTest(unittest.TestCase):
    def test_node_item(self):
        value = 0
        node = Node(value)
        self.assertEqual(value, node.item, msg=f'Node item should be {value}')

    def test_next(self):
        value = 0
        nxt = Node(value)
        node = Node(8, nxt)

        self.assertEqual(value, node.next.item, msg=f'Node next item should be {value}')

    def test_prev(self):
        value = 0
        prev = Node(value)
        node = Node(8, prev=prev)

        self.assertEqual(value, node.prev.item, msg=f'Node prev item should be {value}')


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
    def test_empty_queue(self):
        queue = ArrayQueue()
        self.assertEqual(0, queue.get_size(), msg='Queue should be empty')
        self.assertTrue(queue.is_empty(), msg='Queue should be empty')

    def test_dequeue_empty(self):
        queue = ArrayQueue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue(self):
        queue = ArrayQueue()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        count = 0
        for i, item in enumerate(queue):
            count += 1
            self.assertEqual(lst[i], item, msg='Items should be in the right order')
        self.assertEqual(len(lst), queue.get_size(), msg=f'Queue should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Queue should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(queue), msg='All items added to the Queue should be in the Queue')

    def test_dequeue(self):
        queue = ArrayQueue()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        for e in lst:
            self.assertEqual(e, queue.dequeue(), msg='Items should be in the right order')


class LinkedQueueTest(unittest.TestCase):
    def test_empty_queue(self):
        queue = LinkedQueue()
        self.assertEqual(0, queue.get_size(), msg='Queue should be empty')
        self.assertTrue(queue.is_empty(), msg='Queue should be empty')

    def test_enqueue(self):
        queue = LinkedQueue()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        count = 0
        for item in queue:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        for e, a in zip(lst, list(queue)):
            self.assertEqual(e, a, msg='Should be equal')
        self.assertEqual(len(lst), queue.get_size(), msg=f'Queue should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Queue should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(queue), msg='All items added to the Queue should be in the Queue')

    def test_dequeue(self):
        queue = LinkedQueue()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        for e in lst:
            self.assertEqual(e, queue.dequeue(), msg='Items should be in the right order')

    def test_dequeue_empty(self):
        queue = LinkedQueue()
        with self.assertRaises(AttributeError):
            queue.dequeue()


class ArrayStackTest(unittest.TestCase):
    def test_empty_stack(self):
        stack = ArrayStack()
        self.assertEqual(0, stack.get_size(), msg='Stack should be empty')
        self.assertTrue(stack.is_empty(), msg='Stack should be empty')

    def test_pop_empty(self):
        stack = ArrayStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_push(self):
        stack = ArrayStack()
        lst = range(10)
        for i in lst:
            stack.push(i)
        count = 0
        for i, item in enumerate(stack):
            count += 1
            self.assertEqual(lst[i], item, msg='Items should be in the right order')
        self.assertEqual(len(lst), stack.get_size(), msg=f'Stack should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Stack should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(stack), msg='All items added to the Stack should be in the Stack')

    def test_pop(self):
        stack = ArrayStack()
        lst = range(10)
        for i in lst:
            stack.push(i)
        for e in lst[::-1]:
            self.assertEqual(e, stack.pop(), msg='Items should be in the right order')


class LinkedStackTest(unittest.TestCase):
    def test_empty_stack(self):
        stack = LinkedStack()
        self.assertEqual(0, stack.get_size(), msg='Stack should be empty')
        self.assertTrue(stack.is_empty(), msg='Stack should be empty')

    def test_pop_empty(self):
        stack = LinkedStack()
        with self.assertRaises(AttributeError):
            stack.pop()

    def test_push(self):
        stack = LinkedStack()
        lst = range(10)
        for i in lst:
            stack.push(i)
        count = 0
        lst = lst[::-1]
        for i, item in enumerate(stack):
            count += 1
            self.assertEqual(lst[i], item, msg='Items should be in the right order')
        self.assertEqual(len(lst), stack.get_size(), msg=f'Stack should have {len(lst)} items')
        self.assertEqual(len(lst), count, msg=f'Stack should have {len(lst)} items')
        self.assertSequenceEqual(lst, list(stack), msg='All items added to the Stack should be in the Stack')

    def test_pop(self):
        stack = LinkedStack()
        lst = range(10)
        for i in lst:
            stack.push(i)
        for e in lst[::-1]:
            self.assertEqual(e, stack.pop(), msg='Items should be in the right order')


if __name__ == "__main__":
    unittest.main()
