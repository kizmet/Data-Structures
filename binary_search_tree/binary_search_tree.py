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

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value:
            cb(self.value)
            if self.left:
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)

    """
def in_order_print(self, node):
    print(node)
bst.for_each(bst.in_order_print)
"""
    # DAY 2 Project -----------------------
    # breadth first queue
    # depth first is stack
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        # "1\n2\n3\n4\n5\n6\n7\n8\n"
        # l,d,r
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len():
            current_node = queue.dequeue()  # pop left
            print(current_node.value)  # d
            if current_node.left:
                queue.enqueue(current_node.left)  # l
            if current_node.right:
                queue.enqueue(current_node.right)  # r

        """
        test:
        bst.bft_print(self.bst)
        """

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len():
            current_node = stack.pop()
            print(current_node.value)  # d
            if current_node.left:
                stack.push(current_node.left)  # l
            if current_node.right:
                stack.push(current_node.right)  # r

    # STRETCH Goals -------------------------
    # Note: Research may be required
    # Print In-order recursive DFT
    def pre_order_dft(self, node):  # in order or pre order?
        # "1\n8\n5\n3\n2\n4\n7\n6\n"
        # pre order is d,l,r (topoligical)
        # in-order is l,d,r
        # pre order:
        # d,l,r
        # if node:
        print(node.value)  #
        if node.left:
            self.pre_order_dft(node.left)  # l
        if node.right:
            self.pre_order_dft(node.right)  # r

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # "2\n4\n3\n6\n7\n5\n8\n1\n"
        # l,r,n
        if node:
            self.in_order_print(node.left)
            self.in_order_print(node.right)
            print(node.value)


def a(q):
    return [attr for attr in dir(q) if not attr.startswith("__")]


if __name__ == "__main__":
    bst = BinarySearchTree(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)
    # bst.in_order_print(bst)
    # bst.bft_print(bst)
    # bst.dft_print(bst)
    # bst.post_order_dft(bst)
