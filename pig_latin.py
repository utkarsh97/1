"""
pig_latin.py (6 points)
=====

Write a function called to_pig_latin that translates a word into pig latin. 

http://en.wikipedia.org/wiki/Pig_Latin

IPO for to_pig_latin function
-----
input (parameters): a string
processing: convert the string into pig latin
output (return value): a new string (in pig latin)

Our version of Pig Latin will follow these rules:
-----
* _IGNORE ANY STRING WITH NON-LETTER CHARACTERS_ (including spaces); it should
  just return the original string
* _THIS FUNCTION WILL NOT BREAK A STRING INTO SEPARATE WORDS_
* all letters automatically get converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels? you can check if a character exists within a 
  string of all vowels
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

Example:
-----
print(to_pig_latin(s))
# prints out...
"""

#Utkarsh Parasramka
#10/26/2015
#Section: 010

def is_pig_latin(a):
    if a.isalpha():
        length = len(a)
        if length > 1:
            lower = a.lower()
            first_letter = str(lower[0])
            two_letters = str(lower[0]) + str(lower[1])
            vowel = 'aeiou'
            if first_letter in vowel:
                word = lower + 'way'
            elif two_letters == 'sh':
               word = lower[2:] + 'shay'
            elif two_letters == 'ch':
                word = lower[2:] + 'chay'
            elif two_letters == 'th':
                word = lower[2:] + 'thay'
            elif two_letters == 'qa':
                word = lower[2:] + 'qaay'
            else:
                word = lower[1:] + lower[0] + 'ay'
        elif length == 1:
            word = a.lower()
        else:
            word = a
    else:
        word = a
    return word

"""
#assertions:

print(is_pig_latin('at'))
print(is_pig_latin('chillax'))
print(is_pig_latin('thimble'))
print(is_pig_latin('yolo'))
print(is_pig_latin('u mad bro'))

"""
