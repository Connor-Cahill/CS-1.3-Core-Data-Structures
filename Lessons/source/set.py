#!python

from hashtable import Hashtable

class Set:
    def __init__(self, elements=None):
        """
        inits new instance of our Set class
        with option to pass in items as array
        """
        # NOTE: we can just use the hashtables size counter
        self.data = Hashtable()  # using hashtable to store sets data

        # if elements were passed through
        # fill up our set
        if elements is not None:
            for element in elements:
                self.add(element)


    def contains(self, element):
        """
        Given an element will return true or false
        depending on whether the element is in set
        O(1) ---> b/c we are using a hashtable for
        data so constant read time
        """
        # use hashtables contains method which
        # returns a bool
        return self.data.contains(item)

    def add(self, element):
        """
        Given an  element as arg will add to
        set IF element is not already in set
        in which case will raise ValueError
        O(1)* ---> b/c hashtables are constant
        time to add to unless a resize is necessary
        """
        # check if element is already
        # present in set and raise ValueError
        if self.data.contains(element):
            raise ValueError('Element: {} already in set. No duplicates allowed.'.format(element))

        # element is not in set
        # use hashtable add method
        # set k, v as same TODO: decide to have k == v or k, True
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


    def length(self):
        """returns the length of set"""
        # uses the hashtables lenth method
        return self.data.length()
