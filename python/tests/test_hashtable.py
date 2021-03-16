from challenges.hashtable.hashtable import Hashtable
from challenges.hashtable.class_linked_list import LinkedList

def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('spam')
    secondary = hashtable._hash('spam')
    assert initial == secondary


def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('spam')

    # assert actual >= 0
    # assert actual < hashtable._size

    assert 0 <= actual < hashtable.size


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('listen')
    secondary = hashtable._hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('glisten')
    secondary = hashtable._hash('silent')
    assert initial != secondary

def test_add_and_get():
    hashtable = Hashtable()
    hashtable.add('luci', 'terror')
    actual = hashtable.get('luci')
    expected = 'terror'
    assert actual == expected

def test_contains():
    hashtable = Hashtable()
    hashtable.add('luci', 'terror')
    actual = hashtable.contains('luci')
    expected = True
    assert actual == expected
