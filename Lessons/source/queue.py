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
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()  # uses linkedlist is_empty method

    def length(self):
        """Return the number of items in this queue."""
        return self.list.length()  # use linkedlists length method

    def enqueue(self, item):
        """
        Insert the given item at the back of this queue.
        Running time: O(1) – b/c our linked list has a tail pointer so
        appending is constant [TODO]
        """
        self.list.append(item)  # use linked list append method to add to end

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # returns the head of list and uses linked list is_empty method to
        # check if list is empty, if it is returns None
        return self.list.head if not self.list.is_empty() else None

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # check if queue is empty and throw error
        if self.list.is_empty():
            raise ValueError('Queue is empty')
 
        # grab value of head in linked list
        # and then use linked list delete method
        # on head node
        popped_item = self.list.head.data  # item to be dequeued
        self.list.delete(popped_item)
        return popped_item  # return dequeued item


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
        return len(self.list) == 0  # return true if length is 0

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)  # return length of list

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
            self.list.pop(0)  # remove item
            return popped_item
        else:  # queue is empty
            raise ValueError('cannot dequeue because queue is empty')


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
