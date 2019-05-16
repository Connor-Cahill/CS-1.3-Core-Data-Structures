#!python
# used for traversing iteratively
from stack import LinkedStack
# used for BFS
from queue import LinkedQueue
from binarytree import BinarySearchTree


class MapBSTNode(object):
    """
    Node class for the binary search tree meant to be implemented 
    as buckets in hashtable
    """
    def __init__(self, key, value):
        """Initialize this binary tree node with the given data."""
        self.data = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.right is not None or self.left is not None

    def two_children(self):
        """Returns True if node has 2 children"""
        return self.right is not None and self.left is not None

    def height(self):
        """
        Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: O(n) we are recursing down
        and accounting for every node in tree (or subtree)
        """
        # height of left path down the tree
        left_height = self.left.height() if self.left is not None else -1
        # height of right path
        right_height = self.right.height() if self.right is not None else -1
        # return the greater of the 2 paths
        # add one to account for self
        return 1 + max(left_height, right_height)


class BinarySearchTreeMap(BinarySearchTree):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        super().__init__(items=None)
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def contains(self, item):
        """
        Return True if this binary search tree contains the given item.
        Best case running time: O(log n) the tree is somewhat balanced
        b/c binary search
        Worst case running time: O(n) bst is a linked list
        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, key):
        """
        Return a value in this binary search tree matching the given key,
        or None if the given item is not found.
        Best case running time: O(log n) tree is somewhat balanced
        and it uses binary search
        Worst case running time: O(n) tree is not balanced and is
        linked list
        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(key, self.root)
        # Return the node's data if found, or None
        return node.value if node is not None else None

    def insert(self, key, value):
        """
        Insert the given item in order into this binary search tree.
        Best case running time: O(log n) tree is balanced and it
        can find node position using binary search
        Worst case running time: O(n) tree is unbalanced
        and is linked list
        """
        # Handle the case where the tree is empty
        if self.is_empty():
            # set root node
            self.root = MapBSTNode(key, value)
            # increment size counter
            self.size += 1
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(key, self.root)

        # Check if the given item should be inserted left of parent node
        if key > parent.data:
            parent.right = MapBSTNode(key, value)
        else:  # item is less than or equal to
            parent.left = MapBSTNode(key, value)
        # increment the size counter
        self.size += 1

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """
        Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in the tree
        TODO: Memory usage: O(log n) because we are creating a stack this
        will have at most the same number nodes as height
        of tree from start node
        """
        # check to make sure there is a node
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)

            # Visit this node's data with given function
            visit((node.data, node.value))

            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_recursive(self.root, items.append)
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in the tree
        TODO: Memory usage: O(n) because we are creating a stack
        """

        if node is not None:
            # Visit this node's data with given function
            visit(node.data)
            # Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)
