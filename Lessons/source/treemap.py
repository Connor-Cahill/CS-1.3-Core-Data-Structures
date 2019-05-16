#!python

from map_bst import BinarySearchTreeMap

class TreeMap(object):
    """
    Hashtable with Binary Search Tree as buckets 
    """

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [BinarySearchTreeMap() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """
        Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: O(1) only a few calculations
        need be done
        """
        # return # entries in hashtable divided by total buckets
        return self.size / len(self.buckets)

    def keys(self):
        """
        Return an ordered list of all keys in this hash table.
        Best and worst case running time: O(n) we have to iterate
        over every item in hashtable
        """
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items_in_order():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return an ordered list of all values in this hash table.
        Best and worst case running time: O(n) b/c it requires iterating
       over every entry in hashtable
        """
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items_in_order():
                all_values.append(value)
        return all_values

    def items(self):
        """
        Return a list of all entries (key-value pairs) in order that are
        in this hash table.

        Best and worst case running time: O(n)requires to iterate over every
        entry in the hashtable.
        """
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items_in_order())
        return all_items

    def length(self):
        """
        Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: O(1) there is a size proptery in
        hashtable class that can be returned in constant time
        """
        # returns size counter for hashtable class (counts number of entries)
        return self.size

    def contains(self, key):
        """
        Return True if this hash table contains the given key, or False.
        Best case running time: O(1) constant time to read from hashtable
        Worst case running time: O(n) lots of collisions
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # use BST contains method which returns true or false
        return bucket.contains(key)

    def get(self, key):
        """
        Return the value associated with the given key, or raise KeyError.
        Best case running time: O(1) constant time to read from hashtable
        Worst case running time: O(log n) lots of collisions but tree as bucket
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # use tree's search method and if it returns None throw error
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.search(key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """
        Insert or update the given key with its associated value.
        Best case running time: O(1) constant time adding to normal hashtable
        just have to hash key and put in bucket
        Worst case running time: O(log n)lots of collisions but using bst
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        self.size += 1  # increment size counter
        # use trees contains method to see if entry already exists
        entry = bucket.search(key)
        if entry is not None:  # already in hashtable
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(key)
            self.size -= 1  # decrement again b/c updating old key
        # Insert the new key-value entry into the bucket in either case
        bucket.insert(key, value)
        # Check if the load factor exceeds a threshold such as 0.75
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key):
        """
        Delete the given key and its associated value, or raise KeyError.
        Best case running time: O(1) b/c hash func and key can get us to bucket
        Worst case running time: O(n) lots of collisions and need to iterate
        through linked list
        """
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.search(key)
        if entry is not None:  # item in hashtable
            # Remove the key-value entry from the bucket
            bucket.delete(key)
            self.size -= 1  # decrement size counter
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """
        Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: O(n) iterate through all items to
        rehash all keys and set items
        Best and worst case space usage: O(n) b/c every entry has to be stored
        """
        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size

        # Option to reduce size if buckets are sparsely filled(low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size

        # Get a list to temporarily hold all current key-value entries
        items = self.items()

        # Create a new list of new_size total empty linked list buckets
        self.__init__(new_size)

        # Insert each key-value entry into the new list of buckets,
        for key, value in items:
            self.set(key, value)
        return self  # return updated self

