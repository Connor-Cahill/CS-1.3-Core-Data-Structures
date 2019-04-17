#!python

class DoublyNode(object):

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

    def _get_node_at_index(self, index):
        """
        Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) b/c we could be fetching head item
        Worst case running time: O(n) b/c we have to traverse linked list
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))

        # Check if index is greater or less than half of list size
        # this is so we can initialize are node at either head or tail 
        # and index counter at back or front of list
        if index <= (self.size//2):
            counter = 0
            node = self.head
            direction = "forwards"
        else:
            counter = self.size - 1
            node = self.tail
            direction = "backwards"

        # iterate until the index of item is found
        # we will either be traversing forwards or backwards
        # depending on the above conditional
        while node is not None:
            # check if counter is the index and return item
            if index == counter:
                return node

            # decide which way to traverse list
            if direction == "forwards":
               node = node.next
               counter += 1
            else:
                node = node.prev
                counter -= 1

    def get_at_index(self, index):
        """
        given an index will return the data in
        the node at that index
        """
        # use our private get node at index method
        # then just return the nodes data
        node = self._get_node_at_index(index)
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

        # Use our get_at_index method to grab the node
        # at the index we want to insert
        node = self._get_node_at_index(index)
        # create new node to be inserted
        new_node = DoublyNode(item)

        # shift next and previous pointers on nodes 
        # to add the new node into the list
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
        new_node.next = node
        self.size += 1  # increment size counter


    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        Best and worst case running time: O(1) b/c tail pointer can easily
        grab end item and insert new item at end
        """
        # Create a new node to hold the given item
        new_node = DoublyNode(item)
        # increment size counter
        self.size += 1
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            new_node.prev = self.tail  # new nodes prev is pointing to old tail
            self.tail.next = new_node

        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        Best and worst case running time: O(1) b/c there is a head pointer
        """
        # Create a new node to hold the given item
        new_node = DoublyNode(item)
        # increment size counter
        self.size += 1
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            self.head.prev = new_node  # old heads prev pointer now pointing to new node
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

    def _find_node_by_item(self, item):
        """ given an item returns node """
        # init vars to iterate forwards and backwards
        # these vars hold node and index
        # index is needed for condition in while loop
        forwards = [self.head, 0]
        backwards = [self.tail, (self.size - 1)]

        # traverse list until backwards node
        # equals forwards node (every item has been touched)
        while backwards[1] > forwards[1]:
            if backwards[0].data == item:
                return backwards[0]

            if forwards[0].data == item:
                return forwards[0]

            # grab next nodes in list
            # and update counters
            backwards[0] = backwards[0].prev
            backwards[1] -= 1
            forwards[0] = forwards[0].next
            forwards[1] += 1


        # check if last node checked is item
        # this is necessary b/c while loop could break
        # if backwards and forwards meet in middle
        if forwards[0] is not None:
            if forwards[0].data == item:
                return forwards[0]
        raise ValueError('Item: {} not in list'.format(item))



    def replace(self, old_item, new_item):
        """
        Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: O(1) replacing head or tail
        Worst case running time: O(n) replacing item in middle
        requires traversing linked list
        """
        # use helper function to get node
        # note the helper function will raise ValueError
        # if item is not found in list
        node = self._find_node_by_item(old_item)

        # check that node is something
        if node == None:
            raise ValueError('Item: {} not found in list'.format(old_item))

        # replace data
        node.data = new_item

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) when deleting head or tail
        Worst case running time: O(n) when deleting middle nodes b/c
        this requires traversing through linkedlist.
        """
        # use helper function to find node of item
        node = self._find_node_by_item(item)
        # check if node is something
        if node == None:
            raise ValueError('Item: {} not found in list'.format(item))

        # check if it is head or tail to reassign necessary values
        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        # reassign nodes pointers to skip over node
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        self.size -= 1  # decrement length counter


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
