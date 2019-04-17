#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()  # uses linkedlist is_empty() method

    def length(self):
        """Return the number of items in this stack."""
        # uses linked list length method to return size property
        return self.list.length()

    def push(self, item):
        """
        Insert the given item on the top of this stack.
        Running time: O(1) b/c we are just prepending to linkedlist
        """
        # use linked list prepend method to put on top of stack
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # if stack is not empty return head(top) item else return NONE
        return self.list.head.data if not self.list.is_empty() else None

    def pop(self):
        """
        Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – we can just remove head from linkedlist
        which is constant time
        """
        # check that stack is not empty
        if not self.list.is_empty():
            # grab top item on stack (item to be removed)
            popped_item = self.list.head

            # use linkedlist delete method to remove item
            self.list.delete(popped_item.data)
            return popped_item.data

        else: # stack is empty, raise value error
            raise ValueError('cannot pop from stack because stack is empty')


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # if length of list is 0 (its empty) return true
        return len(self.list) == 0

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)  # use lists length method

    def push(self, item):
        """
        Insert the given item on the top of this stack.
        Running time: O(1) – appending to the end of a list is constant time
        """
        # Note: we are using the end of the list as the "top of stack"
        # this is b/c prepending is too expensive for use of stack
        self.list.append(item)  # append to end of list

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # using index of -1 b/c we are using the 
        # end of the list as top of stack
        return self.list[-1] if not self.is_empty() else None

    def pop(self):
        """
        Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) - b/c popping from end of list is constant time
        """
        # check if stack is empty and raise error
        if self.is_empty():
            raise ValueError('cannot pop because stack is empty')

        # grab value of item at end of list and pop it
        # note using end of list as top of stack
        popped_item = self.list[-1]
        self.list.pop()
        return popped_item  # item just deleted from stack


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
