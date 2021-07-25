"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Class for finding random words from dictionary.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, link):
        '''Read the file'''
        list_file = open(link)
        self.words = self.parse(list_file)
        print( f"{len(self.words)} words read")

    def parse(self, list_file):
        '''Parse the file to get the list of words'''
        return list_file.read().split("\n")
        #return [word.strip() for word in list_file]

    def random(self):
        '''Return the random word in the file'''
        print(random.choice(self.words))


if __name__ == "__main__":
    wf = WordFinder("data/words.txt")
    wf.random()


