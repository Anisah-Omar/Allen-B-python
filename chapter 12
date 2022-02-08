 exercises/12.1.py

def most_frequent(string):
    """
    takes a string
    prints the letters of that string in descending order
    of frequency
    returns nothing
    """
    # format string: remove spaces, make lower
    formatted = string.replace(' ', '').lower()

    # create dict of letters and frequency
    # based on `histogram()` from chapter 11
    hist = dict()
    for char in formatted:
        hist[char] = hist.get(char, 0) + 1

    # reverse keys and values with tuple assignment
    # hist.items() == list of each char and freq as tuples
    freq_list = list()
    for (char, freq) in hist.items():
        freq_list.append((freq, char))

    # sort frequency list
    # `reverse` sorts in descending order
    freq_list.sort(reverse=True)

    # create list of characters by frequency
    char_freq = list()
    for (freq, char) in freq_list:
        char_freq.append(char)

    print(char_freq)
Exercise 12.2
More Anagrams:

Write a program that reads a word list from a file and prints all the sets of words that are anagrams.

example output:

['deltas','desalt','lasted','salted','slated','staled']
['retainers','ternaries']
['generating','greatening']
['resmelts','smelters','termless']
# exercises/12.2.1.py

fin = open("exercises/words.txt")


def word_to_tuple(word):
    """
    takes a word
    returns a tuple of each letter in that word
    sorted alphabetically
    """
    # since strings are sequences of letters
    # `sorted` will automatically convert a string
    # to a list, then sort it
    word = tuple(sorted(word))
    return word


def print_anagrams(anagrams):
    """
    takes a dictionary of lists of words keyed
    to tuples of the letters in those words
    prints any list of words with more than one word in it.
    """
    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1:
            print(words)


def anagrams(word_list):
    """
    takes a list of words
    returns a dictionary containing lists of words
    keyed to tuples of the letters in those words
    """
    output = dict()

    for word in word_list:
        word = word.strip()
        letters = word_to_tuple(word)
        # add letters as key to output dict
        # if not present already
        output[letters] = output.get(letters, [])
        # append word to list at key
        output[letters].append(word)

    return output


print_anagrams(anagrams(fin))
Modify the previous program so that it prints the longest list of anagrams first, followed by the second longest, and so on.

# exercises/12.2.2.py

# ...

def print_anagrams(anagrams):
    
    # ...
    
    sorted_words = list()

    for letter_set in anagrams:
        words = anagrams.get(letter_set)
        if len(words) > 1:
            sorted_words.append(words)

    # sort by length in descending order
    # see: https://docs.python.org/3.7/library/functions.html#sorted
    for set in sorted(sorted_words, key=len, reverse=True):
        print(set)
        
# ...
In Scrabble, a "bingo" is when you play all seven tiles in your rack, along with a letter on the board, to form an eight-letter word. What collection of 8 letters forms the most possible bingos?

# exercises/12.2.3.py

# ...

def print_anagrams(anagrams):
    # ...
    for letter_set in anagrams:
        # ...
        if len(words) > 1 and len(letter_set) == 8:
            # ...

# ...

"""
ANSWER:
	letters = ('a', 'e', 'g', 'i', 'n', 'r', 's', 't')
	words = ['angriest', 'astringe', 'ganister', 'gantries', 'granites', 'ingrates', 'rangiest']
"""
