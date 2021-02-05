

class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Stack():
    # FILO
    def __init__(self, node = None):
        self.top = node
        self.counter = 0
        
    def push(self, value):
        # create node from value
        node = Node(value)
        # point new node to top
        node.next = self.top
        # assign node to top
        self.top = node
        self.counter += 1


    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.top
        self.top = self.top.next
        self.counter -= 1
        return node.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value


class Queue():
    # FIFO
    def __init__(self):
        self.front = None
        self.rear = None
        self.counter = 0
    
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.counter +=1
    
    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        node = self.front
        self.front = self.front.next
        self.counter -= 1
        return node.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

