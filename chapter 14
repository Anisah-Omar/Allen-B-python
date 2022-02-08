Write a module that imports anagram_sets and provides two new functions: store_anagrams should store the anagram dictionary in a "shelf"; read_anagrams should look up a word and return a list of its anagrams.

A 'shelf' is a way to persist dictionary data.

# exercises/14.2.py

import os, shelve

import anagram_sets

def store_anagrams(filepath):
    """
    creates dictionary of anagrams in a list of words
    in a given file at filepath
    stores dictionary in a 'shelf'
    """
    # extract filename from given path
    # for use as shelf file name
    filename = os.path.splitext(filepath)[0]
    anagrams = anagram_sets.all_anagrams(filepath)
    print(anagrams)
    try:
        with shelve.open(filename) as db:
            for key, value in anagrams.items():
                db[key] = value
    except:
        print('error writing to shelf')

def read_anagrams(database, word):
    """
    looks up a given word in a given database
    returns a list of of anagrams for that word
    """
    try:
        with shelve.open(database) as db:
            return db[word]
    except:
        print('error reading from shelf')


# run program
if __name__ == '__main__':
    store_anagrams('exercises/test.txt')
    print(read_anagrams('exercises/test', 'glo'))
Exercise 14.3
In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix(like .mp3).

# exercises/14.3.1.py

import os

def walk(dir, ext=None):
    """
    walks through a given directory and all subdirs
    returns the abspath for any files with the given extension
    if no ext given, returns all files
    """
    for root, dirs, files in os.walk(dir):
        for file in files:
            if ext == None or os.path.splitext(file)[1] == ext:
                print(os.path.abspath(file))

if __name__=="__main__":
    walk('.', '.txt')
To recognize duplicates, you can use md5sum to compute a "checksum" for each file. If two files have the same checksum, they probably have the same contents.

# exercises/14.3.2.py

import hashlib, os

md5_map = dict()

def create_md5_map(dir, ext=None):
    """
    walks through a given directory and all subdirs
    maps md5 checksums to the paths to files with those checksums
    """
    global md5_map
    for root, dirs, files in os.walk(dir):
        for file in files:
            if ext == None or os.path.splitext(file)[1] == ext:
                # add to dict checksum: [filename, filename]
                path = os.path.abspath(file)
                md5 = create_checksum(file)
                md5_map[md5] = md5_map.get(md5, [])
                md5_map[md5].append(path)

def create_checksum(file):
    """
    takes a file
    returns a checksum for that file
    """
    return hashlib.md5(file.encode('utf-8')).hexdigest()

if __name__=="__main__":
    walk('.', '.mp3')
    for key, value in md5_map.items():
        print("{}\t{}".format(key, value))
        
        
