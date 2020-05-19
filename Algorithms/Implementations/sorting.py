from time import time


def selection_sort(items, timeout=60):
    arr = items.copy()
    n = len(arr)
    if 0 <= n <= 1:
        return arr
    start = time()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if time() - start > timeout:
            raise TimeoutError(f'Sorting took longer than {timeout} seconds')
    return arr


def in_place_merge(items, lower, mid, upper):
    temp = items.copy()
    i, j = lower, mid + 1

    for k in range(lower, upper + 1):
        if i > mid:
            items[k], j = temp[j], j + 1
        elif j > upper:
            items[k], i = temp[i], i + 1
        elif temp[j] < temp[i]:
            items[k], j = temp[j], j + 1
        else:
            items[k], i = temp[i], i + 1


def top_down_merge_sort(items):
    arr = items.copy()
    n = len(arr)
    if 0 <= n <= 1:
        return arr

    def sort(a, lower, upper):
        if upper <= lower:
            return
        mid = lower + (upper - lower) // 2
        print(a, lower, mid, upper)
        sort(a, lower, mid)
        sort(a, mid + 1, upper)
        in_place_merge(a, lower, mid, upper)

    sort(arr, 0, n - 1)
    return arr
