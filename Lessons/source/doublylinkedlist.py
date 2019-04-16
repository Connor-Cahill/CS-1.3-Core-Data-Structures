#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """
        Return the length of this linked list by traversing its nodes.
        Best and worst case running time: O(1) b/c we are keeping track
        of number of nodes in size property
        """
        return self.size  # use size property of linked list class

    def get_at_index(self, index):
        """
        Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) b/c we could be fetching head item
        Worst case running time: O(n) b/c we have to traverse linked list
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # init vars for prev node and node
        # grab head (first node)
        node = self.head
        # loop through linked list for range of index
        # stop once you get to index
        for _ in range(index):
            node = node.next
        return node.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if inserting at head or tail
        Worst case running time: O(n) if traversing through linked list
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # edge case: index is 0
        # prepending to linked list
        if index == 0:
            # list empty and index to input is 0
            # assign to head and tail
            self.prepend(item)
            return

        # edge case: index is len(list) (appending)
        if index == self.size:
            self.append(item)
            return  # item added end function

        # check to see if index is
        # in first half of list or second half
        # then choose to traverse backwards or forwards
        if index >= (self.size // 2):
            node = self.tail
        else:
            # grab first node in list
            node = self.head

        # loop range of index to
        # keep grabbing next node in list
        for _ in range(index):
            if node.next is None:
                raise ValueError("Index out of range")
            node = node.next

        # create new node and shift pointers
        # new_node should point to current nodes next
        # current node (node var) will point to new node
        new_node = Node(item)
        new_node.next = node.next
        node.next = new_node
        # added node -> increment size counter
        self.size += 1
        return

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) b/c tail pointer can easily
        grab end item and insert new item at end
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # increment size counter
        self.size += 1
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) b/c there is a head pointer
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # increment size counter
        self.size += 1
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """
        Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) replacing head or tail
        Worst case running time: O(n) replacing item in middle
        requires traversing linked list
        """
        # check if old item is tails data
        # replace data and exit function early
        if self.tail.data == old_item:
            self.tail.data = new_item
            return  # breaks function

        # grab first node in linked list
        node = self.head

        # move through linked list until the node is nothing
        while node is not None:
            # check if node is old item
            # replace item if yes
            if node.data == old_item:
                node.data = new_item
                return  # end function (everything done)

            # grab next node
            node = node.next

        raise ValueError("Item: {} not in linked list".format(old_item))

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) when deleting head or tail
        Worst case running time: O(n) when deleting middle nodes b/c
        this requires traversing through linkedlist.
        """
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # decrement size counter
            self.size -= 1
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
