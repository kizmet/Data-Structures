import sys

sys.path.append("./doubly_linked_list")
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.count = 0
        self.cache = {}
        self.storage = DoublyLinkedList()
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        node = self.cache[key] if key in self.cache else None
        try:
            self.storage.move_to_front(node)
            return node.value[key]
        except:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def addnode(self, key, value):
        cachenode = {key: {key: value}}
        node = cachenode[key]
        self.storage.add_to_head(node)
        self.cache[key] = self.storage.head

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = {key: value}
            self.storage.move_to_front(node)
            return
        elif self.count == self.limit:
            tail = self.storage.tail
            tailkey = list(tail.value.keys())[0]
            del self.cache[tailkey]
            self.storage.remove_from_tail()
            # cachenode = {key: {key: value}}
            # node = cachenode[key]
            # self.storage.add_to_head(node)
            # self.cache[key] = self.storage.head
            self.addnode(key, value)
        else:
            # cachenode = {key: {key: value}}
            # node = cachenode[key]
            # self.storage.add_to_head(node)
            # self.cache[key] = self.storage.head
            self.addnode(key, value)
            self.count += 1

    def __repr__(self):
        return f"count: {self.count}, cache {self.cache} \n storage {self.storage}"


if __name__ == "__main__":
    r = LRUCache(3)
    r.set("item1", "a")
    r.set("item2", "b")
    r.set("item3", "c")
    # r.set("item4", "aa")
    # self.set("item5", "bb")
    # self.set("item6", "cc")
    # self.set("item7", "aaa")
    # self.set("item8", "bbb")
    # self.set("item9", "ccc")
    # self.set("item10", "eee")
    # # add 11th item:
    # self.set("item11", "aaaa")
    # # get item2,set as as head:
    # self.get("item2")
    # print(self.storage.head.value)
    # # set item3 as head:
    # self.set("item3", "c")
    # print(self.storage.head.value)
    # # rewrite item4 as aa2, move to head
    # self.set("item4", "cc4")
    # print(self.storage.head.value)
