from challenges.tree_intersection.tree_intersection import Tree_Intersection
from challenges.tree.tree import Node, BinaryTree


# ******* MY Binary TEST TREE *********
#             [5]
#            /   \
#          [3]    [7]
#         /   \      \
#       [2]   [1]     [6]



def test_happy_path():
    tree1 = BinaryTree()
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
    tree1.root = n6

    tree2 = BinaryTree()
    m1 = Node(2)
    m2 = Node(1)
    m3 = Node(4)
    m4 = Node(8)
    m5 = Node(7)
    m6 = Node(5)    
    m6.left = m4
    m6.right = m5
    m4.left = m1
    m4.right = m2
    m5.right = m3
    tree2.root = m6

    intersect = Tree_Intersection()

    actual = intersect.tree_intersection(tree1, tree2)
    expected = [2, 1, 5, 7]
    assert actual == expected

    