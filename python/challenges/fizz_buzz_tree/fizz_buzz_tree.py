# Roger Note
# class K_node: 
#     def __init__(self, value): 
#         self.key = value 
#         self.child = [] <--- List of childred that the nodes has.



class K_ary_Tree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        new_list = []
        def traverse(root):
            if not root:
                return "No root to be found."
            new_list.append(root.value)
            if root.children != None:
                for child in root.children:
                    traverse(child)
        traverse(self.root)
        return new_list
        
class K_node: 
    def __init__(self, value = None): 
        self.value = value 
        self.children = []

class FizzBuzzTree:
    def __init__(self, root = None):
        self.root = root

    def pre_fizz_buzz(self, tree):
        new_fizzy_tree = K_ary_Tree()
        new_knode = K_node()
        new_fizzy_tree.root = new_knode
        root = tree.root
        def traverse(root, new_knode):
            if not root:
                return "No root to be found."
            
            if root.value % 15 == 0:
                new_knode.value = "FizzBuzz"
            elif root.value % 5 == 0:
                new_knode.value = "Buzz"
            elif root.value % 3 == 0:
                new_knode.value = "Fizz"
            else: 
                new_knode.value = str(root.value)

            if root.children != None:
                for child in root.children:
                    temp_knode = K_node()
                    new_knode.children.append(temp_knode)
                    traverse(child, temp_knode)

        traverse(self.root, new_knode)
        return new_fizzy_tree