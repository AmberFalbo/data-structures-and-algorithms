from class_linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0
        
        for ch in key:
            sum += ord(ch)
        
        primed = sum * 19

        index = primed % self.size

        return index

# using set instead of add in the assignment because wont it call recursivly or error with the add and .add?
    def set(self, key, value):
        pass
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()
        
        self._buckets[hashed_key_index].add((key, value))

    def get(self, requested_key):
        pass


    def contains(self):
        pass