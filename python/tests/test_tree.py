import pytest
from challenges.tree.tree import Node, BinaryTree, BinarySearchTree
import builtins


# ********** BinaryTree Tests ********* 

def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None

# ******* MY Binary TEST TREE *********
#             [5]
#            /   \
#          [3]    [7]
#         /   \      \
#       [2]   [1]     [6]



def test_pre_order_returns_list():
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
    actual = tree.pre_order()
    expected = [5, 3, 2, 1, 7, 6]
    assert actual == expected

def test_in_order_returns_list():
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
    actual = tree.in_order()
    expected = [2, 3, 1, 5, 7, 6]
    assert actual == expected

def test_post_order_returns_list():
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
    actual = tree.post_order()
    expected = [2, 1, 3, 6, 7, 5]
    assert actual == expected

def test_maximum_value_returns_maxval():
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
    actual = tree.find_maximum_value()
    expected = 7
    assert actual == expected

def test_breadth_first_returns_list():
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



# ***** BinarySearchTree Tests ***** 

# **** MY BinarySearch TEST TREE ****
#             [5]
#            /   \
#          [3]    [7]
#         /   \      \
#       [1]   [4]     [9]

