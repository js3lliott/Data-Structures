"""
Binary Search Tree
-------------------
A Binary Search Tree is a collection of nodes arranged in a way where they maintain Binary Search Tree properties.
Each node has a key and an associated value. While searching, the desirted key is compared to the keys
in the BInary Search Tree and if found, the associated value is retrieved.

"""

class BinarySearchTree:
    """
    Implementation of Binary Search Tree
    """

    def __init__(self, data=None):
        self.data = data
        self.root = self
        self.left = None
        self.right = None
        self.parentNode = None

    def isEmpty(self):
        """
        Checks if the node is empty
        """
        return self.root.data is None

    def insert(self, data):
        """
        Inserts an element to the Binary Search Tree
        """
        if self.isEmpty():
            self.root = BinarySearchTree(data)
            return

        if self.data < data:
            if self.right is None:
                self.right = BinarySearchTree(data)
                self.right.parentNode = self
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = BinarySearchTree(data)
                self.left.parentNode = self
            else:
                self.left.insert(data)

    def find(self, data):
        """
        Finding an element in the Binary Search Tree
        """

        if self.data == data:
            return True
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        else:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    
    def in_order(self):
        """
        Traverses the tree in order
        """
        
        if self.left != None:
            self.left.in_order()
        print(self.data, end=", ")
        if self.right != None:
            self.right.in_order()

    def pre_order(self):
        """
        Traverses the tree in pre-order
        """

        print(self.data, end=", ")
        if self.left != None:
            self.left.pre_order()
        if self.right != None:
            self.right.pre_order()


    def post_order(self):
        """
        Traverses the tree in post-order
        """

        if self.left != None:
            self.left.pre_order()
        if self.right != None:
            self.right.pre_order()
        print(self.data, end=", ")

def _check(minimum, root, maximum):
    if root is None:
        return True
    if not minimum < root.data < maximum:
        return False
    return _check(minimum, root.left, root.data) and _check(root.data, root.right, maximum)

def validate_bst(root):
    """
    Validate the binary search tree
    """
    infinity = 10**10
    return _check(-infinity, root, infinity)