#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    # index for iterating backwards through string
    backwards = len(text) - 1
    # index for iterating forward through string
    forwards = 0
    while backwards > forwards:
        # check that the items are letters
        # if not skip items until is letter
        if not text[forwards].isalpha():
            forwards += 1
            continue
        if not text[backwards].isalpha():
            backwards -= 1
        # the pointers have crossed
        # all items in list have been touched
        if backwards <= forwards:
            break
        if text[backwards].lower() != text[forwards].lower():
            # items dont match up, text not palindrone
            return False
        # change our index counters
        forwards += 1
        backwards -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # if left is none function was just called
    # skip down to recursion
    if left is not None:
        # base case: all items have been searched
        # text is a palindrome
        if left > right:
            return True
        # letters do not match
        if text[left].lower() != text[right].lower():
            # item is not letter
            # keep skipping until it is
            if not text[left].isalpha():
                return is_palindrome_recursive(text, left + 1, right)
            if not text[right].isalpha():
                return is_palindrome_recursive(text, left, right - 1)
            return False
        return is_palindrome_recursive(text, left + 1, right - 1)
    return is_palindrome_recursive(text, 0, len(text) - 1)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
