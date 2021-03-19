from ..hashtable.class_linked_list import LinkedList
from ..hashtable.hashtable import Hashtable
from ..tree.tree import BinaryTree


class Tree_Intersection:

    def __init__(self):
        self.self = self

    def tree_intersection(self, tree1, tree2):
        hashtable = Hashtable()
        hashtable = self.traverse1(tree1.root, hashtable)
        repeat_values = []
        repeat_values = self.traverse2(tree2.root, repeat_values, hashtable)

        return repeat_values

    def traverse1(self, root, hashtable):
        if root.left is not None:
            self.traverse1(root.left, hashtable)
        hashtable.add(str(root.value), root.value)
        if root.right is not None:
            self.traverse1(root.right, hashtable)
        return hashtable

    def traverse2(self, root, repeat_values, hashtable):
        if root.left is not None:
            self.traverse2(root.left, repeat_values, hashtable)
        if hashtable.contains(str(root.value)):
            repeat_values.append(root.value)
        if root.right is not None:
            self.traverse2(root.right, repeat_values, hashtable)
        return repeat_values
