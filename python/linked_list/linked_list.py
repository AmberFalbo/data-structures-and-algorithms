class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def insert(self, value):
    node = Node(value)  

    if self.head is not None:
        node.next = self.head
    self.head = node 


    def some_method(self):
        # method body here
        pass
