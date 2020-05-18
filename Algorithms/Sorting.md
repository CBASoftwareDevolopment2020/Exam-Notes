# Sorting

## Knowledge

### _knows_ the basic data structures `Bag`, `Queue`, and `Stack`

| Method  | `Bag`       | `Queue`     | `Stack`     |
|---------|-------------|-------------|-------------|
| add     | `add()`     | `enqueue()` | `push()`    |
| remove  |             | `dequeue()` | `pop()`     |
| isEmpty | `isEmpty()` | `isEmpty()` | `isEmpty()` |
| size    | `getSize()` | `getSize()` | `getSize()` |

#### `Bag`

![Operations on a `Bag`](../images/Operations_on_a_bag.PNG)

A `Bag` is a collection where removing item is not supported, its purpose is to provide the ability to collect items
and then iterate through the collected items. It also include the ability to test if the `Bag` is empty and find the
number of items. The order of iteration is unspecified.  
In [`bag.py`](Implementations/bag.py) two implementations can be found, one that uses an `Array` to store the items,
and one that uses a `Linked List`.

#### `Queue`

![A typical FIFO `Queue`](../images/A_typical_FIFO_queue.PNG)

A `Queue` is a collection that is based on the first-in-first-out policy. When iterating through a `Queue`, the items
are processed in the order they where added to the `Queue`.  
In [`queue.py`](Implementations/queue.py) two implementations can be found, one that uses a `List` to store the items,
and one that uses a `Linked List`.

#### `Stack`

![Operations on a pushdown `Stack`](../images/Operations_on_a_pushdown_stack.PNG)

A `Stack` is a collection that is based on the last-in-first-out policy. When iterating through a `Stack`, the items
are processed in reverse of the order in which they where added.  
In [`stack.py`](Implementations/stack.py) two implementations can be found, one that uses a `List` to store the items,
and one that uses a `Linked List`.

### _knows_ selection sort and its complexity

1. set the first item in the unsorted array as minimum
2. find minimum in the rest of the unsorted array
3. swap the first item with minimum
4. repeat until index equals length

![](../images/Trace_of_selection_sort.PNG)

<table>
    <tr>
        <td style="text-align:center;" colspan="4">Selection Sort</td>
    </tr>
    <tr>
        <td style="text-align:center;" colspan="3">Time Complexity</td>
        <td>Space Complexity</td>
    </tr>
    <tr>
        <td>Best Case</td>
        <td>Average Case</td>
        <td>Worst Case</td>
        <td>Worst Case</td>
    </tr>
    <tr>
        <td>O(n<sup>2</sup>)</td>
        <td>O(n<sup>2</sup>)</td>
        <td>O(n<sup>2</sup>)</td>
        <td>O(1)</td>
    </tr>
</table>



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
