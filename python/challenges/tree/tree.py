class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

# preOrder
    def pre_order(self):
        def traverse(root):
            # if there is no node there then exit
            if not root:
                return
            # print root first
            print(root.value)
            # traverse left
            traverse(root.left)
            # traverse right
            traverse(root.right)
        traverse(self.root)

# inOrder
    def in_order(self):
        def traverse(root):

            # traverse left
            if root.left:
                traverse(root.left)
            print(root.value)
            # traverse right
            if root.right:
                traverse(root.right)
        traverse(self.root)

# postOrder
    def post_order(self):
        def traverse(root):

            # traverse left
            if root.left:
                traverse(root.left)
            # traverse right
            if root.right:
                traverse(root.right)
            print(root.value)
        traverse(self.root)

class BinarySearchTree(BinaryTree):
    def __init__(self, root = None):
        self.root = root

    # def add(self, value):
    #   def traverse(root, value):

    #       if self.root.value:
    #           if value < self.root.value:
    #               if self.root.left is None:
    #                   self.root.left = Node(value)
    #               else:
    #                   self.root.left = Node(value)
    #           elif value > self.root.value:
    #               if self.root.right is None:
    #                   self.root.right = Node(value)
    #               else:
    #                   self.root.right = Node(value)
    #       else:
    #           self.value = value
    #   traverse(self.root)

    def contains(self,value):
        # return true if the value is in the tree or false otherwise
        pass

# if __name__ == "__main__":

#     a = Node("A")        
#     b = Node("B")        
#     c = Node("C")        
#     d = Node("D")        
#     e = Node("E")        
#     f = Node("F")   

#     b.left = d
#     b.right = e
#     c.left = f

#     tree = BinaryTree(Node("A"))
#     tree = BinarySearchTree(Node("A"))
#     tree.root.left = b
#     tree.root.right = c 
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.root.left.left.value)
    # tree.pre_order()
    # tree.in_order()
    # tree.post_order()

    # ******
    # tree.add('d')
    # actual = 'd'
    # expected = tree.root.right.right.value
    # assert actual == expected
    # ******