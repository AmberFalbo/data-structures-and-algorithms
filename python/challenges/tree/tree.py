from ..stacks_and_queues.stacks_and_queues import Queue

class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

# Pre-order: root >> left >> right
# preOrder
    def pre_order(self, action = None):
        new_list = []
        def traverse(root, action):
            # root_array.append(root.value)
            # if there is no node there then exit
            if not root:
                return "No root to be found."

            # print root first
            # print(root.value)
            # for action do this instead**all action just added
            action(root.value)
            # adding to list
            new_list.append(root.value)
            if root.left != None:
                # traverse left
                traverse(root.left, action)
            
            if root.right != None:
                # traverse right
                traverse(root.right, action)

        traverse(self.root, action or print)
        return new_list

# In-order: left >> root >> right
# inOrder
    def in_order(self):
        def traverse(root):
            if not root:
                return "No root to be found."
                                
            new_list = []

            # traverse left
            if root.left:
                traverse(root.left)
            print(root.value)
            # traverse right
            if root.right:
                traverse(root.right)
        traverse(self.root)

# Post-order: left >> right >> root
# postOrder
    def post_order(self):
        def traverse(root):
            if not root:
                return "No root to be found."

            # root array
            # root_array = []

            # traverse left
            if root.left:
                traverse(root.left)
            # traverse right
            if root.right:
                traverse(root.right)
            print(root.value)
        traverse(self.root)


# find maximum value in a tree
    def find_maximum_value(self):
        max_value = self.root.value
        def traverse(root):

            nonlocal max_value

            if root.value > max_value:
                max_value = root.value

            if root.left:
                traverse(root.left)

            if root.right:
                traverse(root.right)
        traverse(self.root)
        return max_value

    def breadth_first(self):
        q = Queue()
        new_list = []

        node = self.root
        q.enqueue(node)
        while q.counter > 0:
            node = q.dequeue()
            new_list.append(node.value)
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
        return new_list    




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

if __name__ == "__main__":

    a = Node("A")        
    b = Node("B")        
    c = Node("C")        
    d = Node("D")        
    e = Node("E")        
    f = Node("F")   

    b.left = d
    b.right = e
    c.left = f

    tree = BinaryTree(Node("A"))
    tree = BinarySearchTree(Node("A"))
    tree.root.left = b
    tree.root.right = c 
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.root.left.left.value)
    # tree.pre_order()
    # tree.in_order()
    # tree.post_order()
    tree.find_maximum_value()

    # ******
    # tree.add('d')
    # actual = 'd'
    # expected = tree.root.right.right.value
    # assert actual == expected
    # ******