from time import time
from random import choice, randint, shuffle


def selection_sort(arr, timeout=60):
    n = len(arr)
    if 0 <= n <= 1:
        return
    start = time()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if time() - start > timeout:
            raise TimeoutError(f'Sorting took longer than {timeout} seconds')


def insertion_sort(arr, timeout=60):
    n = len(arr)
    if 0 <= n <= 1:
        return
    start = time()
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            if time() - start > timeout:
                raise TimeoutError(f'Sorting took longer than {timeout} seconds')


def merge_sort(arr):
    def merge(l, r):
        new = []
        left_idx = right_idx = data_idx = 0
        left_len, right_len = len(l), len(r)

        while left_idx < left_len and right_idx < right_len:
            if l[left_idx] < right[right_idx]:
                new.append(l[left_idx])
                left_idx += 1
            else:
                new.append(r[right_idx])
                right_idx += 1
            data_idx += 1

        while left_idx < left_len:
            new.append(l[left_idx])
            left_idx += 1
            data_idx += 1
        while right_idx < right_len:
            new.append(r[right_idx])
            right_idx += 1
            data_idx += 1

        return new

    data = arr[:]
    n = len(data)
    if n < 2:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    data = merge(left, right)
    return data


def quick_sort(items):
    arr = items.copy()
    n = len(arr)
    if 0 <= n <= 1:
        return arr
    shuffle(arr)
    # if the sub array has 15 items or less use insertion sort
    if n <= 15:
        insertion_sort(arr)
        return arr
    else:
        idx = randint(0, n - 1)
        arr[0], arr[idx] = arr[idx], arr[0]
        pivot = arr[0]
        less = []
        greater = []

        for x in arr[1:]:
            if x < pivot:
                less.append(x)
            else:
                greater.append(x)

        return quick_sort(less) + [pivot] + quick_sort(greater)


def quick_sort_3way(items):
    arr = items.copy()
    n = len(arr)
    if 0 <= n <= 1:
        return arr
    shuffle(arr)
    # if the sub array has 15 items or less use insertion sort
    if n <= 15:
        insertion_sort(arr)
        return arr
    else:
        pivot = choice(arr)
        less = []
        equal = []
        greater = []

        for x in arr:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)

        return quick_sort_3way(less) + equal + quick_sort_3way(greater)


def heapify(data, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data[left] > data[largest]:
        largest = left
    if right < n and data[right] > data[largest]:
        largest = right

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)


def heap_sort(arr):
    n = len(arr)
    if n < 2:
        return arr

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr
