#!python

from linkedlist import LinkedList
from linkedlist import Node


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        # holds count of how many elements are in queue (keeps length method constant)
        self.size = 0
        # set head and tail of Queue
        self.head = None
        self.tail = None
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.head is None # returns true if nothing is in head

    def length(self):
        """Return the number of items in this queue."""
        return self.size # returns value of queue's size property

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # create new node with given item
        new_tail =  Node(item)
        self.size += 1 # increment size counter
        # check that list is not empty
        if not self.is_empty():
            # grab current tail in queue
            current_tail = self.tail
            self.tail = new_tail
            # set the old tail's next to point towards new tail
            current_tail.next = new_tail
        else: # queue was empty:
            # when queue is empty we need to
            # add the new item as the head and tail of our queue
            self.head = new_tail
            self.tail = new_tail

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # head is the front most node in queue
        return self.head.data  if not self.is_empty() else None
    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # check if queue is empty
        if not self.is_empty():
            current_head = self.head
            # shift head to the next node in quueue (will be None if nothing)
            self.head = current_head.next
            self.size -= 1 # decrement size counter
            return current_head.data # item that was just removed
        else: # queue is empty
            raise ValueError('Cannot dequeue item because queue is empty')

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return len(self.list) == 0 # return true if length is 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list) # return length of list

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # append item to end of list
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # returns first item in list unless list is empty then return NONE
        return self.list[0] if not self.is_empty() else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # check that queue is not empty
        if not self.is_empty():
            # grab value of item to be popped from queue
            popped_item = self.list[0]
            self.list.pop(0) # remove item
            return popped_item
        else: # queue is empty
            raise ValueError('cannot dequeue because queue is empty')


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
