from ..hashtable.class_linked_list import LinkedList
from ..hashtable.hashtable import Hashtable
import re

class RepeatedWord:

    def __init__(self):
        self.self = self
        

    def repeat_word(self, phrase):
        phrase = re.sub(r'[^\w\s]', '', phrase)
        phrase = phrase.lower()
        words = phrase.split()
        hashtable = Hashtable()

        for word in words:
            if hashtable.contains(word):
                return word
            else:
                hashtable.add(word, word)
        return None
        

