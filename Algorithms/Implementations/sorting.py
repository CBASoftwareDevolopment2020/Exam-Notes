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
