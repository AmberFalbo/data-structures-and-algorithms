from challenges.linked_list.linked_list import LinkedList, Node
import pytest


def test_import():
    assert LinkedList
    assert Node

def test_str():
    test_list = LinkedList()
    test_list.append(8)
    test_list.append(6)
    test_list.append(7)
    test_list.append(5)
    test_list.append(3)
    test_list.append(0)
    test_list.append(9)
    actual = test_list.__str__()
    expected = f'{{ 8 }} -> {{ 6 }} -> {{ 7 }} -> {{ 5 }} -> {{ 3 }} -> {{ 0 }} -> {{ 9 }} -> None'
    assert actual == expected


def test_insert():
    test_list = LinkedList() 
    test_list.insert(3)
    actual = test_list.head.value
    expected = 3
    assert actual == expected   

# add a node to the end of the linked list
def test_append():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> None'
    assert actual == expected

# insert a node before a node located in the middle of a linked list
def test_insert_before():
    node = Node(0)
    link = LinkedList(node)
    link.insert(4)
    link.append(10)
    link.insert_before(0,5)
    actual = str(link)
    expected = f'{{ 4 }} -> {{ 5 }} -> {{ 0 }} -> {{ 10 }} -> None'
    assert actual == expected

# def test_insert_after():
#     node = Node(0)
#     link = LinkedList(node)
#     link.insert(4)
#     link.append(10)
#     link.insert_after(10, 5)
#     actual = str(link)
#     expected = f'{{ 4 }} -> {{ 0 }} -> {{ 10 }} -> {{ 5 }} ->  None'
#     assert actual == expected


@pytest.fixture
def generate_new_list():
    node = Node(0)
    new_list = LinkedList(node)
    list_length = 0

    for value in range(1,5):
        new_list.insert(value)
        list_length += 1

    return new_list