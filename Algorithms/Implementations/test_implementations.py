from random import choices, shuffle
import unittest

from bag import ArrayBag, LinkedBag
from heap import MaxHeap
from queue import ArrayQueue, LinkedQueue
from sorting import heap_sort, insertion_sort, merge_sort, quick_sort, quick_sort_3way, selection_sort
from stack import ArrayStack, LinkedStack
from utils import IOHandler, is_sorted, Node, print_heap


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.ds = Node

    def test_node_item(self):
        value = 0
        node = self.ds(value)
        self.assertEqual(value, node.item, msg=f'Node item should be {value}')

    def test_next(self):
        value = 0
        nxt = self.ds(value)
        node = self.ds(8, nxt)

        self.assertEqual(value, node.next.item, msg=f'Node next item should be {value}')

    def test_prev(self):
        value = 0
        prev = self.ds(value)
        node = self.ds(8, prev=prev)

        self.assertEqual(value, node.prev.item, msg=f'Node prev item should be {value}')


class ArrayBagTest(unittest.TestCase):
    def setUp(self):
        self.ds = ArrayBag

    def test_empty_bag(self):
        bag = self.ds(10)
        self.assertEqual(0, bag.get_size(), msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = self.ds(10)
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
        bag = self.ds(capacity)
        for i in range(10):
            bag.add(i)
        with self.assertRaises(IndexError):
            bag.add(10)


class LinkedBagTest(unittest.TestCase):
    def setUp(self):
        self.ds = LinkedBag

    def test_empty_bag(self):
        bag = self.ds()
        self.assertEqual(0, bag.get_size(), msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = self.ds()
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
    def setUp(self):
        self.ds = ArrayQueue

    def test_empty_queue(self):
        queue = self.ds()
        self.assertEqual(0, queue.get_size(), msg='Queue should be empty')
        self.assertTrue(queue.is_empty(), msg='Queue should be empty')

    def test_dequeue_empty(self):
        queue = self.ds()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_enqueue(self):
        queue = self.ds()
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
        queue = self.ds()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        for e in lst:
            self.assertEqual(e, queue.dequeue(), msg='Items should be in the right order')


class LinkedQueueTest(unittest.TestCase):
    def setUp(self):
        self.ds = LinkedQueue

    def test_empty_queue(self):
        queue = self.ds()
        self.assertEqual(0, queue.get_size(), msg='Queue should be empty')
        self.assertTrue(queue.is_empty(), msg='Queue should be empty')

    def test_enqueue(self):
        queue = self.ds()
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
        queue = self.ds()
        lst = range(10)
        for i in lst:
            queue.enqueue(i)
        for e in lst:
            self.assertEqual(e, queue.dequeue(), msg='Items should be in the right order')

    def test_dequeue_empty(self):
        queue = self.ds()
        with self.assertRaises(AttributeError):
            queue.dequeue()


class ArrayStackTest(unittest.TestCase):
    def setUp(self):
        self.ds = ArrayStack

    def test_empty_stack(self):
        stack = self.ds()
        self.assertEqual(0, stack.get_size(), msg='Stack should be empty')
        self.assertTrue(stack.is_empty(), msg='Stack should be empty')

    def test_pop_empty(self):
        stack = self.ds()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_push(self):
        stack = self.ds()
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
        stack = self.ds()
        lst = range(10)
        for i in lst:
            stack.push(i)
        for e in lst[::-1]:
            self.assertEqual(e, stack.pop(), msg='Items should be in the right order')


class LinkedStackTest(unittest.TestCase):
    def setUp(self):
        self.ds = LinkedStack

    def test_empty_stack(self):
        stack = self.ds()
        self.assertEqual(0, stack.get_size(), msg='Stack should be empty')
        self.assertTrue(stack.is_empty(), msg='Stack should be empty')

    def test_pop_empty(self):
        stack = self.ds()
        with self.assertRaises(AttributeError):
            stack.pop()

    def test_push(self):
        stack = self.ds()
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
        stack = self.ds()
        lst = range(10)
        for i in lst:
            stack.push(i)
        for e in lst[::-1]:
            self.assertEqual(e, stack.pop(), msg='Items should be in the right order')


class MaxHeapTest(unittest.TestCase):
    def setUp(self):
        self.ds = MaxHeap

    def test_empty_heap(self):
        mh = self.ds(0)
        self.assertEqual(0, mh.get_size(), msg='Heap should be empty')
        self.assertTrue(mh.is_empty(), msg='Heap should be empty')

    def test_dequeue_empty(self):
        mh = self.ds(0)
        with self.assertRaises(IndexError):
            mh.remove_max()

    def test_enqueue(self):
        mh = self.ds(32)
        lst = list(range(1, 32))
        shuffle(lst)
        for i in lst:
            mh.insert(i)
        items = []
        for _ in range(mh.get_size()):
            val = mh.remove_max()
            items.append(val)
            print(val,items)
            print_heap(mh.Heap)
        self.assertEqual(len(lst), len(items), msg=f'Heap should have {len(lst)} items')
        self.assertSequenceEqual(sorted(lst, reverse=True), items,
                                 msg='All items added to the Heap should be in the Heap')

        def test_dequeue(self):
            queue = self.ds()
            lst = range(10)
            for i in lst:
                queue.enqueue(i)
            for e in lst:
                self.assertEqual(e, queue.dequeue(), msg='Items should be in the right order')

    class SelectionSortTest(unittest.TestCase):
        def setUp(self):
            self.alg = selection_sort

        def test_sort_empty(self):
            actual = expected = []
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('SORTEXAMPLE'), list('AEELMOPRSTX')
            self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_timeout(self):
            expected = list(range(1_000_000))
            shuffle(expected)
            with self.assertRaises(TimeoutError):
                self.alg(expected, timeout=1)

        def test_sort_shakespeare(self):
            words = IOHandler('../../Assets/Files/shakespeare-complete-works.txt').words
            self.assertTrue(len(words) > 0)
            with self.assertRaises(TimeoutError):
                self.alg(words)

    class InsertionSortTest(unittest.TestCase):
        def setUp(self):
            self.alg = insertion_sort

        def test_sort_empty(self):
            actual = expected = []
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('SORTEXAMPLE'), list('AEELMOPRSTX')
            self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            self.alg(expected)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_timeout(self):
            expected = list(range(1_000_000))
            shuffle(expected)
            with self.assertRaises(TimeoutError):
                self.alg(expected, timeout=1)

        def test_sort_shakespeare(self):
            words = IOHandler('../../Assets/Files/shakespeare-complete-works.txt').words
            self.assertTrue(len(words) > 0)
            with self.assertRaises(TimeoutError):
                self.alg(words)

    class MergeSortTest(unittest.TestCase):
        def setUp(self):
            self.alg = merge_sort

        def test_sort_empty(self):
            actual = expected = []
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('MERGESORTEXAMPLE'), list('AEEEEGLMMOPRRSTX')
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_shakespeare(self):
            shakespeare = IOHandler('../../Assets/Files/shakespeare-complete-works.txt')
            actual, expected = shakespeare.words, shakespeare.sorted_words
            self.assertTrue(len(actual) > 0)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

    class QuickSortTest(unittest.TestCase):
        def setUp(self):
            self.alg = quick_sort

        def test_sort_empty(self):
            actual = expected = []
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('MERGESORTEXAMPLE'), list('AEEEEGLMMOPRRSTX')
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_shakespeare(self):
            shakespeare = IOHandler('../../Assets/Files/shakespeare-complete-works.txt')
            actual, expected = shakespeare.words, shakespeare.sorted_words
            self.assertTrue(len(actual) > 0)
            with self.assertRaises(RecursionError):
                actual = self.alg(actual)

    class QuickSort3WayTest(unittest.TestCase):
        def setUp(self):
            self.alg = quick_sort_3way

        def test_sort_empty(self):
            actual = expected = []
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('MERGESORTEXAMPLE'), list('AEEEEGLMMOPRRSTX')
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_shakespeare(self):
            shakespeare = IOHandler('../../Assets/Files/shakespeare-complete-works.txt')
            actual, expected = shakespeare.words, shakespeare.sorted_words
            self.assertTrue(len(actual) > 0)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

    class HeapSortTest(unittest.TestCase):
        def setUp(self):
            self.alg = heap_sort

        def test_sort_empty(self):
            actual = expected = []
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_one(self):
            actual = expected = [1]
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort(self):
            actual, expected = list('MERGESORTEXAMPLE'), list('AEEEEGLMMOPRRSTX')
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_large(self):
            expected = list(range(2 ** 10))
            actual = expected[:]
            shuffle(actual)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sorted(self):
            actual = expected = list(range(10))
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

        def test_sort_shakespeare(self):
            shakespeare = IOHandler('../../Assets/Files/shakespeare-complete-works.txt')
            actual, expected = shakespeare.words, shakespeare.sorted_words
            self.assertTrue(len(actual) > 0)
            actual = self.alg(actual)
            self.assertEqual(expected, actual)
            self.assertCountEqual(expected, actual)
            self.assertSequenceEqual(expected, actual)

    if __name__ == "__main__":
        unittest.main()
