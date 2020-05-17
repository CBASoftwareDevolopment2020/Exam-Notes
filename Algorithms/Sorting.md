# Sorting

## Knowledge

### _knows_ the basic data structures `Bag`, `Queue`, and `Stack`

#### `Bag`

A `Bag` is a collection where removing item is not supported, its purpose is to provide the ability to collect items and then iterate through the collected items. It also include the ability to test if the `Bag` is empty and find the number of items.  
In [`bag.py`](Implementations/bag.py) two implementations can be found, one that uses an `Array` to store the items, and one that uses a `Linked List`.

#### `Queue`

#### `Stack`

### _knows_ selection sort and its complexity

| Index  |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |
|--------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Init   | __6__ |   4   | __1__ |   8   |   9   |   2   |   7   |   5   |   3   |
| Iter 1 |  _1_  | __4__ |   6   |   8   |   9   | __2__ |   7   |   5   |   3   |
| Iter 2 |  _1_  |  _2_  | __6__ |   8   |   9   |   4   |   7   |   5   | __3__ |
| Iter 3 |  _1_  |  _2_  |  _3_  | __8__ |   9   | __4__ |   7   |   5   |   6   |
| Iter 4 |  _1_  |  _2_  |  _3_  |  _4_  | __9__ |   8   |   7   | __5__ |   6   |
| Iter 5 |  _1_  |  _2_  |  _3_  |  _4_  |  _5_  | __8__ |   7   |   9   | __6__ |
| Iter 6 |  _1_  |  _2_  |  _3_  |  _4_  |  _5_  |  _6_  | __7__ |   9   |   8   |
| Iter 7 |  _1_  |  _2_  |  _3_  |  _4_  |  _5_  |  _6_  |  _7_  | __9__ | __8__ |
| Iter 8 |  _1_  |  _2_  |  _3_  |  _4_  |  _5_  |  _6_  |  _7_  |  _8_  |  _9_  |

O(n<sup>2</sup>)


### _knows_ the concept of divide and conquer algorithms and their complexity

### _knows_ the difference between time and space complexity

### _knows_ what defines a stable sorting algorithm

### _knows_ the purpose of `sink` and `swim` functions

## Abilities

### is _able_ to explain complexity in algorithms using big-O notation

### is _able_ to implement insertion sort and knows its complexity

### is _able_ to explain heaps and head sort

## Skills

### have the _skills_ to select the best implementation of simple data structures

### have the _skills_ to choose the right algorithm for a problem, based on stability and complexities

### have the _skills_ to choose the right priority queue implementation
