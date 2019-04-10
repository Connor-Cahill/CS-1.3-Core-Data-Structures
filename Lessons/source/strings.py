#!python
from collections import deque


def contains(text: str, pattern: str) -> bool:
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # matched keeps track of matched letters
    matched = ''
    # if pattern is larger than text
    # raise error. incorrect inputs
    if len(pattern) > len(text): 
        raise ValueError("pattern cannot be larger than text inputs")
    # edge case: empty string
    if len(pattern) == 0:
        return True
    # loop over text to compare letter to
    # letter in pattern
    for letter in text:
        if letter == pattern[len(matched)]:
            matched += letter
        else:
            matched = ''
            # check if letter matched first letter in pattern
            if letter == pattern[len(matched)]:
                matched += letter
        # if matched is equal to pattern
        # the pattern was in the text
        if matched == pattern:
            return True
    return False

def find_index(text: str, pattern: str, start=0) -> (int, None):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # edge case: pattern is longer text than text
    if len(pattern) > len(text):
        return None
    # edge case: patten is empty string
    if len(pattern) == 0:
        return 0
    # case: pattern equals text:
    # pattern is in text and starting index would be 0
    if pattern == text:
        return start
    # keeps track of start index and will be returned value
    start_index = ''
    # keeps track of matched letters between pattern and text
    matched = ''
    for i in range(start, len(text)):
        letter = text[i]
        if letter == pattern[len(matched)]:
            # matched is empty, this is currently start_index
            if len(matched) == 0:
                start_index = i
            matched += letter
        else:
            matched = ''
            if letter == pattern[len(matched)]:
                start_index = i
                matched += letter
        # if matched is pattern then
        # pattern was found in text
        if matched == pattern:
            return start_index
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # vars to keep track of start_indexes
    # and returned value from find_index
    start_indexes = []
    found_index = ''
    # check if text is same as pattern
    if text == pattern:
        return [0]
    # edge case: pattern is empty
    if pattern == found_index:
        return [i for i in range(len(text))]
    start = 0
    # call out find_index function and slice the text inputted
    while found_index is not None or found_index != len(text) - (len(pattern) - 1): 
        found_index = find_index(text, pattern, start)
        if found_index is not None:
            # turns index back into index from OG text
            # by using length of pattern and start_indexes
            # (to tell us how many times list was sliced)
            start_indexes.append(found_index)
            # make sure there is more text to keep checking
            if found_index == len(text) - (len(pattern) - 1):
                return start_indexes
            start = found_index + 1
        else:
            break
    return start_indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    test_string_algorithms('abc', 'abc')
