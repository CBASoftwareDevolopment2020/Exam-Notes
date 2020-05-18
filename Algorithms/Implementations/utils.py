class Node:
    def __init__(self, item, next=None, prev=None):
        self.item = item
        self.next = next
        self.prev = prev

    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return self.item == other.item

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        # return f'{self.item} -> {self.next}'
        return str(self.item)
