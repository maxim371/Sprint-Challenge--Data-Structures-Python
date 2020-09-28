"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def isEmpty(self):
        return self.storage == []    
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):  #0(1) - add to end of queue
        self.storage.append(value)

    def dequeue(self):         #FIFO - remove starting brginning of queue
        data = self.storage[0]
        del self.storage[0]
        return data


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def isEmpty(self):
        return self.storage == []    

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        data = self.storage[-1]
        del self.storage[-1]
        return data


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
                return
            else:
                return self.right.insert(value)
        else:
            value < self.value
            if self.left is None:
                self.left = BSTNode(value)
                return
            else:
                return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        else:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # if self is not None:
        #     return
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        ans = ''
        while q:
            curr = q.dequeue()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            q.enqueue(curr.left)
            q.enqueue(curr.right)
        print(ans[:-1])

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def bft_print(self, node):
        stack = Stack()
        stack.push(node)
        ans = ''
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            ans += str(curr.value) + '\n'
            stack.push(curr.right)
            stack.push(curr.left)
        print(ans[:-1])

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# # print("elegant methods")
# # print("pre order")
# # bst.pre_order_dft()
# # print("in order")
# # bst.in_order_dft()
# # print("post order")
# # bst.post_order_dft()  
