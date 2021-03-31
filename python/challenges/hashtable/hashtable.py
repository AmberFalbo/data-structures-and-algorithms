from .class_linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def _hash(self, key):
        sum = 0
        for ch in key:
            sum += ord(ch)
            # sum = sum + ord(ch)
        
        primed = sum * 19
        index = primed % self.size

        return index

    def add_hash(self, key, value):
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()
        
        self._buckets[hashed_key_index].add((key, value))

    def get(self, requested_key):
        index = self._hash(requested_key)

        if self._buckets[index]:
            current = self._buckets[index].head
            while current:
                if current.data[0] == requested_key:
                    return current.data[1]
                current = current.next
            # return self._buckets[index].head.data[1]

    def contains(self, key):
        for i in range(len(self._buckets)):
            if self._buckets[i]:
                current = self._buckets[i].head
                while current:
                    if current.data[0] == key:
                        return True
                    current = current.next
        return False



