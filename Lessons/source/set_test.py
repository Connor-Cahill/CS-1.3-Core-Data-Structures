#!python

from set import Set
import unittest
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


class SetTest(unittest.TestCase):

    def test_init(self):
        test_set = Set(['bob', 'jenn', 'kev'])
        assert test_set.length() == 3  # should have 3 items
        assert test_set.data.length() == 3

    def test_init_with_duplicate(self):
        test_set = Set(['bob', 'bob', 'carl'])  # duplicates! not good
        assert test_set.length() == 2  # should't add repeating value

    # should return True
    def test_contains_is_true(self):
        test_set = Set(['bob', 'jane', 'carl', 'chico'])
        assert test_set.length() == 4  # should be 4 names
        assert test_set.contains('bob') is True

    def test_contains_is_false(self):
        test_set = Set(['bob', 'jane', 'colin', 'dan'])
        assert test_set.length() == 4
        assert test_set.contains('connor') is False  # connor not in set

    def test_empty_contains(self):
        set = Set(['bob', 'jane', 'colin'])
        assert test_set.length() == 3
        assert test_set.contains('') is False

    def test_add(self):
        test_set = Set()
        set.add('bob')
        assert test_set.length() == 1
        assert test_set.contains('bob') is True  # bob is in set
        test_set.add('jane')
        assert test_set.length() == 2  # set has 2 names in it now
        test_set.add('will')
        assert test_set.length() == 3

    # should raise error
    def test_add_duplicates(self):
        test_set = Set()
        test_set.add('bob')
        assert test_set.length() == 1
        test_set.add('bob')
        assert test_set.length() == 1  # should't add repeating value

    def test_remove(self):
        test_set = Set(['bob', 'joe', 'jane', 'donna'])
        assert test_set.length() == 4
        test_set.remove('joe')  # removing joe
        assert test_set.length() == 3  # set is smaller now

    # test remove passing in item not in set
    def test_remove_no_item(self):
        test_set = Set(['dan', 'colin', 'jane', 'chico', 'ozzie'])
        assert test_set.length() == 5
        with self.assertRaises(KeyError):
            test_set.remove('connor')  # connor is not in set

    def test_union(self):
        test_set = Set(['bob', 'jane', 'smith', 'hi'])
        other_set = Set(['jimmy', 'jim', 'kid'])
        assert test_set.union(other_set).length() == 7  # the union should have 7 elements

    def test_union_duplicates(self):
        test_set = Set(['bob', 'jane', 'smith', 'hi'])
        other_set = Set(['jane', 'jim', 'kid'])
        assert test_set.union(other_set).length() == 6  # because repeating element

    def test_intersect(self):
        test_set = Set(['kid', 'jane', 'smith', 'hi'])
        other_set = Set(['jane', 'jim', 'kid'])
        assert test_set.intersection(other_set).length() == 2  # 2 intersecting values

    def test_intersect_none(self):
        test_set = Set(['bob', 'tom', 'smith', 'hi'])
        other_set = Set(['jane', 'jim', 'kid'])
        assert test_set.intersection(other_set).length() == 0  # no intersecting elements

    def test_difference(self):
        test_set = Set(['bob', 'tom', 'smith', 'hi'])
        other_set = Set(['jane', 'bob', 'jim', 'kid'])
        assert test_set.difference(other_set).length() == 3

    def test_difference_no_diff(self):
        test_set = Set(['bob', 'tom', 'smith', 'hi'])
        other_set = Set(['tom', 'bob', 'smith', 'hi'])
        assert test_set.difference(other_set).length() == 0  # no difference 

    def test_is_subset_true(self):
        test_set = Set(['bob', 'tom', 'smith', 'hi', 'football', 'baseball', 'something'])
        other_set = Set(['tom', 'bob', 'smith', 'hi'])
        assert other_set.is_subset(set) is True  # set should be a subset

    def test_is_subset_false(self):
        test_set = Set(['hike', 'tom', 'smith', 'hi'])
        other_set = Set(['tom', 'bob', 'smith', 'hi', 'hope, fun'])
        assert test_set.is_subset(other_set) is False


if __name__ == '__main__':
    unittest.main()
