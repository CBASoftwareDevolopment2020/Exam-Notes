from bag import ArrayBag, LinkedBag, Node
import unittest


class ArrayBagTest(unittest.TestCase):
    def test_empty_bag(self):
        bag = ArrayBag(10)
        self.assertEqual(0, bag._size, msg='Bag should be empty')
        self.assertTrue(bag.is_empty(), msg='Bag should be empty')

    def test_add(self):
        bag = ArrayBag(10)
        bag.add(1)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag._size, msg=f'Bag should have {count} items')
        self.assertSequenceEqual([1], list(bag), msg='All items added to the bag should be in the Bag')

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
        bag.add(1)
        count = 0
        for item in bag:
            count += 1
            self.assertIsNotNone(item, msg='Item should not be None')
        self.assertEqual(count, bag._size, msg=f'Bag should have {count} items')
        self.assertSequenceEqual([Node(1)], list(bag), msg='All items added to the bag should be in the Bag')


if __name__ == "__main__":
    unittest.main()
