"""
lousy_plasma.py (15 points)
=====
See instructions on course site.
"""

#Utkarsh Parasramka
#12/07/2015
#Section: 010

import random
dictionary = open("thesaurus.txt", 'r')
thesaurus_ = dictionary.read()
clean_thesaurus = thesaurus_.strip()
word_list = clean_thesaurus.split('\n')
thesaurus = {}
for line in word_list:
    words_with_syn = line.split(',')
    synonyms = words_with_syn[1:]
    thesaurus[words_with_syn[0]] = synonyms
dictionary.close()
phrase = open('bad_blood.txt', 'r')
lyrics = phrase.read()
lyrics_ = lyrics.strip()
cleaned = ''
for letter in lyrics_:
    if letter.isalpha() or letter == ' ' or letter == '\n':
        cleaned += letter.lower()
words = cleaned.split(' ')
for i in range(0,len(words),2):
    if words[i] in thesaurus:
        k = len(thesaurus[words[i]])
        key = random.randint(0,k-1)
        synonyms = thesaurus[words[i]]
        words[i] = synonyms[key].upper()
    else:
        continue
song = ' '.join(words)
print(song)
from os import system
system("say -i -v Fiona " + "\"" + song + "\"")
