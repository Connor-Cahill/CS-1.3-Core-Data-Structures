#!python

from hashtable import HashTable

class Set:
    def __init__(self, elements=None):
        """
        inits new instance of our Set class
        with option to pass in items as array
        """
        # NOTE: we can just use the hashtables size counter
        self.data = HashTable()  # using hashtable to store sets data

        # if elements were passed through
        # fill up our set
        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """ prints string representation of self"""
        print('SET({})'.format(self.elements()))

    def __repre__(self):
        """ prints self """
        print('SET({})'.format(self.elements()))

    @property
    def size(self):
        return self.data.size

    def contains(self, element):
        """
        Given an element will return true or false
        depending on whether the element is in set
        O(1) ---> b/c we are using a hashtable for
        data so constant read time
        """
        # use hashtables contains method which
        # returns a bool
        return self.data.contains(element)

    def add(self, element):
        """
        Given an  element as arg will add to
        set IF element is not already in set
        in which case will break method early
        O(1)* ---> b/c hashtables are constant
        time to add to unless a resize is necessary
        """
        # check if element is already
        # present in set and return out of method early
        if self.data.contains(element):
            return

        # element is not in set
        # use hashtable add method
        self.data.set(element, element)

    def remove(self, element):
        """
        Given an element will remove from Set if present.
        If element is not in set will return value error
        O(1) ---> b/c hashtables have contant time for deleting
        """
        # use hashtables delete method
        # raises KeyError if element is not present
        self.data.delete(element)

    def elements(self):
        """
        Returns list of elements in set
        to be iterated over
        """
        # returning keys from hashtable
        # b/c key == value in set
        return self.data.keys()

    def length(self):
        """returns the length of set"""
        # uses the hashtables lenth method
        return self.data.length()

    def union(self, other_set):
        """
        Given another set as argument will return
        a new set that is the union of the 2
        (union meaning all elements in both sets)
        O(n + m) ---> b/c it requires to iterate over
        every element in both sets
        """
        # iterate over the 2 sets
        # adding every element to return set
        union = [item for item in self.elements()]
        union.extend(item for item in other_set.elements())
        return Set(union)

    def intersection(self, other_set):
        """
        Given another set as an argument will return
        all overlapping values from both as a new set
        O(n) ---> b/c iterating over every item in the larger
        set to see which to add to return set
        """
        intersection_set = Set()  # set to be returned
        # large is the larger of the 2 sets
        # this way we can only iterate over 1 set
        large = self if self.length() >= other_set.length() else other_set
        small = self if self.length() < other_set.length() else other_set

        # iterate over the larger set and check
        # what values it has in common with smaller set
        # if a value overlaps add it to return set
        # NOTE: keys method is from hashtable class
        for element in large.elements():
            if small.contains(element):  # Both contain element!
                intersection_set.add(element)

        return intersection_set

    def difference(self, other_set):
        """
        Returns a set of elements in this set but not the other_set

        """
        # set to be returned
        diff_set = Set()
        # iterate of this set and add
        # all elements not in other set
        # to our return set
        for element in self.elements():
            if not other_set.contains(element):
                diff_set.add(element)

        return diff_set


    def is_subset(self, other_set):
        """
        Given another set as a argument returns a bool
        on whether this set is a subset of other_set
        O(n) ---> iterate over every item in other set
        to see if they are all in this set
        """
        # if this set is larger than other set
        # it cannot be a subset
        if other_set.length() < self.length():
            return False

        # iterate over smaller set
        for element in self.elements():
            if not other_set.contains(element):
                return False

        # if loop is completed every element
        # from other_set was in this set
        # it is a subset
        return True

