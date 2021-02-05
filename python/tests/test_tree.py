# from challenges.tree.tree import __version__
import pytest
from challenges.tree.tree import Node, BinaryTree, BinarySearchTree
import builtins

# def test_version():
#     assert __version__ == '0.1.0'

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None


def test_breadth_first_search():
    tree = BinaryTree()
    n1 = Node(2)
    n2 = Node(1)
    n3 = Node(6)
    n4 = Node(3)
    n5 = Node(7)
    n6 = Node(5)
    n6.left = n4
    n6.right = n5
    n4.left = n1
    n4.right = n2
    n5.right = n3
    tree.root = n6
    actual = tree.breadth_first()
    expected = [5, 3, 7, 2, 1, 6]
    assert actual == expected