# from challenges.tree.tree import __version__
import pytest
from challenges.tree.tree import Node, BinaryTree, BinarySearchTree

# def test_version():
#     assert __version__ == '0.1.0'

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None

def test_pre_order():
    tree = BinaryTree()
    tree.add('root')
    tree.add('left')
    tree.add('right')
    actual = []
    tree.pre_order(actual.append)
    expected = ['root', 'left', 'right']
    assert actual == expected
    # assert tree.root == 'root'
    # assert tree.left == 'left'
    # assert tree.right == 'right'

#       root
#     /      \
#   left    right

