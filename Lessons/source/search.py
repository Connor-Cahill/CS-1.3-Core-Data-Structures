#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_recursive(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array: [int], item: int, index=0) -> (int, None):
    """Searches for given item in array returns 1st indx of item."""
    # base case: index out of range
    if index == len(array):
        return None
    # base case: arr at index is item
    elif array[index] == item:
        return index
    else:
        # keep looking for item
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array: [int], item: int) -> (int, None):
    """return index of item in sorted array or None if item is not found"""
    # start index at mid index of array
    index = len(array) // 2
    print(index)
    while array != []:
        print(array)
        # index contains item
        if array[index] == item:
            return index
        # check if item in index is larger than item
        elif array[index] > item:
            # cut off greater half of array
            array = array[:index - 1]
        # check if item in index is less than item
        elif array[index] < item:
            # cut off smaller half of arr
            array = array[index + 1:]
        # reset the index to mid point
        index = len(array) // 2
        print(index)
    # item not found
    return None





def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests


if __name__ == '__main__':
    print(binary_search_iterative(['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie'], 'Winnie'))
