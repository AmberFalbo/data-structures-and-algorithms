import pytest
from challenges.quick_sort.quick_sort import quick_sort


def test_quick_sort_happy():
    test_array = [8,4,23,42,16,15]
    actual = quick_sort(test_array, 0, 5)
    expected = [4,8,15,16,23,42]
    assert actual == expected


def test_quick_sort_reverse():
    test_array = [20,18,12,8,5,-2]
    actual = quick_sort(test_array, 0, 5)
    expected = [-2,5,8,12,18,20]
    assert actual == expected    

def test_quick_sort_few_unique():
    test_array = [5,12,7,5,5,7]
    actual = quick_sort(test_array, 0, 5)
    expected = [5,5,5,7,7,12]
    assert actual == expected    

def test_quick_sort_nearly_sorted():
    test_array = [2,3,5,7,13,11]
    actual = quick_sort(test_array, 0, 5)
    expected = [2,3,5,7,11,13]
    assert actual == expected    
