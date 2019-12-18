import sys

sys.path.append("../queue_and_stack")
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:  # value =2
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            # self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value == target:
        #     return True
        # elif self.left == None and bst.right == None:
        #     return False
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            return True

        # [attr for attr in dir(q) if attr.startswith("")]

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


def a(q):
    return [attr for attr in dir(q) if not attr.startswith("__")]


if __name__ == "__main__":
    bst = BinarySearchTree(5)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    print(bst.left.right.value)  # should print 3
    print(bst.right.left.value)  # should print 6
    bst.insert(1)
    bst.insert(4)
    bst.insert(8)
    bst.insert(9)
    # first node
    print(
        bst.contains(5),
        # right, right of node
        bst.contains(7),
        # left, right of node
        bst.contains(3),
    )
