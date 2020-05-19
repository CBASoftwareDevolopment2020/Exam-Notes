from time import time


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


def in_place_merge(arr, lower, mid, upper):
    temp = arr.copy()
    i, j = lower, mid + 1

    for k in range(lower, upper + 1):
        if i > mid:
            arr[k], j = temp[j], j + 1
        elif j > upper:
            arr[k], i = temp[i], i + 1
        elif temp[j] < temp[i]:
            arr[k], j = temp[j], j + 1
        else:
            arr[k], i = temp[i], i + 1


def top_down_merge_sort(arr):
    n = len(arr)
    if 0 <= n <= 1:
        return

    def sort(a, lower, upper):
        if upper <= lower:
            return
        # if the sub array has 15 items or less use insertion sort
        if upper - lower <= 15:
            insertion_sort(a)
        else:
            mid = lower + (upper - lower) // 2
            sort(a, lower, mid)
            sort(a, mid + 1, upper)
            if a[mid] > a[mid + 1]:
                in_place_merge(a, lower, mid, upper)

    sort(arr, 0, n - 1)


def bottom_up_merge_sort(arr):
    n = len(arr)
    for size in range(1, n):
        for lower in range(0, n - size, 2 * size):
            in_place_merge(arr, lower, lower + size - 1, min(lower + 2 * size - 1, n - 1))
        size += size
