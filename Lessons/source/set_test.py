#!python

from set import Set
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        set = Set(['bob', 'jenn', 'kev'])
        assert set.length() == 3  # should have 3 items
        assert set.data.length() == 3

    def test_init_with_duplicate(self):
        with self.assertRaises(ValueError):
            set = Set(['bob', 'bob', 'carl'])  # duplicates! not good

    # should return True
    def test_contains_is_true(self):
        set = Set(['bob', 'jane', 'carl', 'chico'])
        assert set.length() == 4  # should be 4 names
        assert set.contains('bob') is True

    def test_contains_is_false(self):
        set = Set(['bob', 'jane', 'colin', 'dan'])
        assert set.length() == 4
        assert set.contains('connor') is False  # connor not in set

    def test_add(self):
        set = Set()
        set.add('bob')
        assert set.length() == 1
        assert set.contains('bob') is True  # bob is in set
        set.add('jane')
        assert set.length() == 2  # set has 2 names in it now
        set.add('will')
        assert set.length() == 3

    # should raise error
    def test_add_duplicates(self):
        set = Set()
        set.add('bob')
        assert set.length() == 1
        with self.assertRaises(ValueError):
            set.add('bob')  # adding duplicate, should be error

    def test_remove(self):
        set = Set(['bob', 'joe', 'jane', 'donna'])
        assert set.length() == 4
        set.remove('joe')  # removing joe
        assert set.length() == 3  # set is smaller now

    # test remove passing in item not in set
    def test_remove_no_item(self):
        set = Set(['dan', 'colin', 'jane', 'chico', 'ozzie'])
        assert set.length() == 5
        with self.assertRaises(KeyError):
            set.remove('connor')  # connor is not in set

if __name__ == '__main__':
    unittest.main()
