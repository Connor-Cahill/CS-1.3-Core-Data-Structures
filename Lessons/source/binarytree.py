#!python
# used for traversing iteratively
from stack import LinkedStack
# used for BFS
from queue import LinkedQueue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
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


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """
        Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best and worst case running time: O(n) it has to recursively call
        the height method on every node while traversing down trees
        """
        return self.root.height() if not self.is_empty() else 0

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

    def search(self, item):
        """
        Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(log n) tree is somewhat balanced
        and it uses binary search
        Worst case running time: O(n) tree is not balanced and is
        linked list
        """
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
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
            self.root = BinaryTreeNode(item)
            # increment size counter
            self.size += 1
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)

        # Check if the given item should be inserted left of parent node
        if item > parent.data:
            parent.right = BinaryTreeNode(item)
        else:  # item is less than or equal to
            parent.left = BinaryTreeNode(item)
        # increment the size counter
        self.size += 1

    def _find_node_iterative(self, item):
        """
        Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: O(log n) b/c every time we check a node
        we eliminate half of the options
        TODO: Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList
        """
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif node.data < item:
                # Descend to the node's left child
                node = node.left
                continue
            # Check if the given item is greater than the node's data
            elif node.data > item:
                # Descend to the node's right child
                node = node.right
                continue
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """
        Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: O(log n) b/c every time we check a node
        we eliminate half of the options
        TODO: Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList
        """
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # Check if the given item matches the node's data
        elif node.data == item:
            # Return the found node
            return node
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: O(log n) b/c every time we check a node
        we eliminate half of the options
        TODO: Worst case running time: O(n) if tree is very unbalanced it could
        hold structure of LinkedList
        """
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if node.data == item:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
                continue
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
                continue
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # Check if the given item matches the node's data
        if node.data == item:
            # Return the parent of the found node
            return parent
        # Check if the given item is less than the node's data
        elif item < node.data:
            # Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)
        # Check if the given item is greater than the node's data
        elif item > node.data:
            # Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: O(log n) when looking for item everytime
        we check node we eliminate half of the options
        TODO: Worst case running time: O(n) tree is really unbalanced and
        takes linked list structure
        """
        # see if node exists in tree and grab value or 
        # return value error
        node = self._find_node_recursive(item, self.root)
        if node is None:
            raise ValueError("Item: {} not in tree.".format(item))

        # check if node is a leaf
        # if True find the parent of the node and
        # figure out if it is left child or right child
        elif node.is_leaf():
            parent = self._find_parent_recursive(item, self.root)
            if node == parent.left:
                parent.left = None
            else:
                parent.right = None

        # check if case where the node has 2 children
        # then find successor to replace with and shift pointers
        elif node.two_children():
            successor = self._find_successor(node)
            s_parent = self._find_parent_recursive(successor.data, node)
            # replace data w/ successor
            node.data = successor.data
            # deletes the successor node
            s_parent.left = successor.right

        # check case branch has one child
        # just skip over node and grab child
        elif node.is_branch():
            parent = self._find_parent_node_recursive(item, self.root)
            # check what side child the node is to parent
            # and skip over
            if parent.left == node:
                # assign parent to nodes child
                parent.left = node.right if node.right is not None else node.left
            elif parent.right == node:
                parent.right = node.right if node.right is not None else node.right

        # decrement size counter
        self.size -= 1


    def _find_successor(self, start_node):
        """
        Returns successor node in binary tree
        """
        node = start_node
        # if right child is there
        # traverse right down tree
        if node.right is not None:
            node = node.right
        # while there is left children we traverse
        # left down subtree
        while node.left is not None:
            node = node.left
        return node



    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            # self._traverse_in_order_recursive(self.root, items.append)
            self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """
        Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in the tree
        TODO: Memory usage: O(n) because we are creating a stack
        """
        # check to make sure there is a node
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_in_order_recursive(node.left, visit)
            # Visit this node's data with given function
            visit(node.data)
            # Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """
        Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in the tree
        TODO: Memory usage: O(n) because we are creating a stack
        """
        # stack for holding horizon
        stack = LinkedStack()
        # tells when we are done traversing
        done = False
        # set node as start node to start
        current = node
        # traverse nodes while stack is not empty
        while not done:
            # traverse down left side of tree
            # appending nodes to stack
            if current is not None:
                stack.push(current)
                current = current.left

            # if node is none time to go grab
            # from stack
            else:
                # if stack is not empty pop and grab
                # top item in stack
                if not stack.is_empty():
                    current = stack.pop()
                    # visit the node
                    visit(current.data)
                    # grab the right node (None is fine)
                    current = current.right
                else:
                    # All done!
                    done = True


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

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in the tree
        TODO: Memory usage: O(n) because we are creating a stack
        """
        # stack to use to store nodes in order
        stack = LinkedStack()
        # set current to the starting node
        current = node
        # load starting node into stack
        stack.push(current)
        # traverse until stack is empty
        while not stack.is_empty():
            # pop and visit top node in stack
            current = stack.pop()
            visit(current.data)

            # NOTE: right is first because we are using stack
            # so right child will be under left child
            # if right child is present add to stack
            if current.right is not None:
                stack.push(current.right)

            # if left child is present add to stack
            if current.left is not None:
                stack.push(current.left)



    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """
        Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) because every node is visited
        TODO: Memory usage: O(n) we are calling recursion on every node
        """
        # check that node is not none
        if node is not None:
            # Traverse left subtree, if it exists
            self._traverse_post_order_recursive(node.left, visit)
            # Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
            # Visit this node's data with given function
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) because every node is visited
        TODO: Memory usage: O(n) we are creating a stack that will hold
        every node at some point
        """
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """
        Return a level-order list of all items in this binary search tree.
        """
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n) we visit every node in tree
        TODO: Memory usage: O(n) we are creating a queue that every node
        will populate at a certain time
        """
        # Create queue to store nodes not yet traversed in level-order
        queue = LinkedQueue()
        # Enqueue given starting node
        queue.enqueue(start_node)
        # Loop until queue is empty
        while not queue.is_empty():
            # Dequeue node at front of queue
            node = queue.dequeue()
            # Visit this node's data with given function
            visit(node.data)
            # Enqueue this node's left child, if it exists
            if node.left is not None:
                queue.enqueue(node.left)
            # Enqueue this node's right child, if it exists
            if node.right is not None:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
