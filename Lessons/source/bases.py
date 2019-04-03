#!python

"""
Bases.py contains function for converting and working with bases.

Decode: takes in number and converts to base 10
Encode: takes in number in base 10 and converts to another base
Convert: converts number from 1 base to another base
"""

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
int_to_string = string.digits + string.ascii_lowercase

str_to_int = {string: index for index, string in enumerate(int_to_string)}


def decode(digits: str, base: int) -> int:
    """Decode given digits in given base to number in base 10."""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # decimal sum that will be returned
    dec_sum = 0
    # i = index and v = value
    for i, v in enumerate(reversed(digits)):
        dec_sum += (base**i) * str_to_int[v]
    return dec_sum


def encode(number: int, base: int) -> str:
    """Encode given number in base 10 to digits in given base."""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # number to be returned
    new_base = ''
    # find largest whole number log smaller than number
    if number > 0:
        lg_power = math.floor(math.log(number, base))
    else:
        return '0'
    # looping backwards (-1 for 3rd arg) including 0 (-1 for 2nd arg)
    for i in range(lg_power, -1, -1):
        # check if base to power of temp_num less than number
        if base**i <= number:
            # create number to add to return val
            temp_num = number // (base**i)
            # sutbract temp number from number
            number -= temp_num * (base**i)
            new_base += int_to_string[temp_num]
        else:
            # add 0 to output string
            new_base += '0'
    return new_base


def convert(digits: str, base1: int, base2: int) -> str:
    """Convert given digits in base1 to digits in base2."""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # decode digits, base1 into binary, then encode into given base
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    print(decode('10', 10))
