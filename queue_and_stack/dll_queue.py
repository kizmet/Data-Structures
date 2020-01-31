import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # `enqueue` should add an item to the back of the queue.
        # append to the tail?
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # `dequeue` should remove and return an item from the front of the queue.
        # popleft, from the head?
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        # `len` returns the number of items in the queue.
        return self.size


def h(q):
    return [attr for attr in dir(q) if not attr.startswith("__")]


if __name__ == "__main__":
    q = Queue()
    # q.enqueue(5)
    # q.enqueue(4)
    # q.enqueue(3)
    q.dequeue()
