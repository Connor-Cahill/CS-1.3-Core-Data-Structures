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
        appending is constant
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
        Running time: O(1) – b/c linked list class has a
        head pointer we can easily remove first item
        """
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
        """
        Insert the given item at the back of this queue.
        Running time: O(1) – appending to end of list
        is constant time
        """
        # append item to end of list
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # returns first item in list unless list is empty then return NONE
        return self.list[0] if not self.is_empty() else None

    def dequeue(self):
        """
        Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – b/c popping the first element
        is list requires every element after it to shift left
        """
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


### deque implementation

class Deque:

    def __init__(self, items=None):
        """
        initializes a Deque with items if any are given.
        If items are given they are populated into Deque with
        push_front method (loading in front by default)
        """
        # initialize linked list for our deque to use
        self.list = LinkedList()

        # build are deque
        if items is not None:
            for item in items:
                self.push_front(item)

    def push_front(item):
        """
        Takes in given item and prepends it
        to the front of the deque
        """
        # use linked list prepend method
        self.list.prepend(item)

    def push_back(item):
        """
        Takes an item as parameter and appends it
        to the back of the deque
        """
        # uses linked list append method
        self.list.append(item)

    def pop_front():
        """
        Removes the item at front of deque
        and returns it
        """
        # grab item to be popped/returned
        popped_item = self.list.head

        # remove from left side of list using linkedlist delete method
        # note: this is still constant b/c popped_item is first item in linkedlist
        self.list.delete(popped_item)

        return popped_item  # returning item that was just deleted

    def pop_back():
        """
        Removes the item at the end of deque
        and returns its value
        """
        # grab item to be removed (tail of linked list)
        popped_item = self.list.tail

        # remove item from right side
        # TODO: this could be much better with doubly linked list
        # currently O(n)
        self.list.delete(popped_item)

        return popped_item  # return value of deleted item


