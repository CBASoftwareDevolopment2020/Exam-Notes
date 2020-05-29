import re


class Node:
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    # def __eq__(self, other):
    #     if type(other) is not type(self):
    #         return False
    #     return self.item == other.item
    #
    # def __repr__(self):
    #     return self.__str__()
    #
    # def __str__(self):
    #     # return f'{self.item} -> {self.next}'
    #     return str(self.item)


def is_sorted(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    else:
        return True


class IOHandler:
    def __init__(self, path: str):
        self.words = self.read_file(path)
        self.sorted_words = sorted(self.words)

    @staticmethod
    def read_file(path: str) -> list:
        with open(path, encoding="utf-8-sig") as f:
            content = f.read()
        return IOHandler.sanitize_string(content)

    @staticmethod
    def sanitize_string(content: str) -> list:
        content = content.lower()
        return re.findall("[a-z']+", content)


def swim(a, k):
    while k > 1 and k // 2 < k:
        a[k // 2], a[k] = a[k], a[k // 2]
        k //= 2


def sink(a, k, n):
    while 2 * k <= n:
        j = 2 * k
        if j < n and j < j + 1:
            j = j + 1
        if k >= j:
            break
        a[k], a[j], k = a[j], a[k], j


def print_heap(a):
    items_per_line = [1]
    x = 0
    acc = 0
    while acc < len(a):
        n = 2 ** (x + 1)
        items_per_line.append(n)
        x += 1
        acc += n

    i = 1
    idx = 1
    for line in items_per_line:
        string = '  '.join([str(x) for x in a[idx:idx + line]])
        idx += line
        print(string)
        i += 1
