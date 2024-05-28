# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word_letter =sorted([x for x in word])

    def match(self, list):
        #have an empty list
        new_list = []
        #if the word we are testing is in the list it is appended to our empty list
        for item in list:
            if self.word_letter == sorted([y for y in item]):
                new_list.append(item)
        return new_list        