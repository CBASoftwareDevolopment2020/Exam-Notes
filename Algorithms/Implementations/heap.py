from utils import print_heap
from random import shuffle
import sys


class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    # Function to return the position of parent for the node currently at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of the left child for the node currently at pos
    def left_child(self, pos):
        return 2 * pos

    # Function to return the position of the right child for the node currently at pos
    def right_child(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed node is a leaf node
    def is_leaf(self, pos):
        if self.size // 2 <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def max_heapify(self, pos):
        # If the node is a non-leaf node and smaller than any of its child
        if not self.is_leaf(pos):
            if self.Heap[pos] < self.Heap[self.left_child(pos)] or self.Heap[pos] < self.Heap[self.right_child(pos)]:
                # Swap with the left child and heapify the left child
                if self.Heap[self.left_child(pos)] > self.Heap[self.right_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.max_heapify(self.left_child(pos))
                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, self.right_child(pos))
                    self.max_heapify(self.right_child(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element
        current = self.size
        while self.Heap[current] > self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to remove and return the maximum element from the heap
    def remove_max(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.max_heapify(self.FRONT)
        return popped


if __name__ == '__main__':
    maxHeap = MaxHeap(32)
    nums = list(range(1, 32))
    shuffle(nums)

    for i in nums:
        maxHeap.insert(i)

    items = []
    for _ in range(32):
        val = maxHeap.remove_max()
        items.append(val)
        print(val, items)
        print_heap(maxHeap.Heap)
        print('---')
