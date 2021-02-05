class Node:

    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self, head = None):
        self.head = head


    def __str__(self):
        output = ''
        current = self.head

        while current is not None:
            output += f'{{ {current.value} }} -> '
            current = current.next
        return output + 'None'

    def insert(self, value):
        # node = Node(value)

        # if self.head is not None:
        #     node.next = self.head
        # self.head = Node

        self.head = Node(value, self.head)
    
    def includes(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        
        return False

    def append(self,value):
        new_node = Node(value)
        current = self.head

        if self.head is None:
            self.head = new_node
            return
        while current.next is not None:
            current = current.next
        
        current.next = new_node
        return 

    
    def insert_before(self, value, new_val):
        new_node = Node(new_val)
        current = self.head

        # checking for empty list
        if current is None:
            self.insert(new_node)
            return
        while current.next is not None:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
            current = current.next
            return

    def insert_after(self, value, new_val):
        new_node = Node(new_val)
        current = self.head
        
        if current is None:
            self.insert(new_node)
            return

        while current is not None:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            return





if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    print(new_linked)

    new_linked1 = LinkedList(new_node)
    new_linked1.insert(2)

    print(new_linked.includes(10))
    print(new_linked1)


    