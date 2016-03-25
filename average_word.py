"""
average_word.py - 7 points
=====
Write a program that asks the user for words... and prints out the longest
word, the shortest word, and the average length of all of the words entered.

* Generate a random number between 3 and 6, inclusive - this will determine
  how many words to ask for.
* Say: "I'll need [number] words:"
* Proceed to ask for each word, one at a time: "Word #[number] please!"
* At the end, your program should print out:
    * the longest word (the most recently entered longest if there is a tie)
    * the shortest word (the most recently entered shortest if there is a tie)
    * the average length of all of the words
    * if all of the words are the same, then the longest and shortest word
      should be the same!
* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

Hint 1: what data do you need to keep track of in order to meet the
        requirements above?
Hint 2: how can you get the first word entered to be the longest and shortest?
        would it be helpful to do that?
Hint 3: sometimes intializing to an empty string, "", is useful
Hint 4: the empty string, "", has a length of 0
Hint 5: thankfully, words can't be a negative length!
Hint 6: YOU DON'T HAVE TO STORE ALL THE WORDS to determine which one is the
        longest and the shortest... think about the minimum you'd need to
        keep track of...

Example output below; everything after a greater than sign (>) is user input.

Run 1:
-----
I'll need 4 words:
Word #1 please!
> wow
Word #2 please!
> oh
Word #3 please!
> amazing
Word #4 please!
> program
Shortest: oh
Longest: program
Average Length: 4.75

Run 2:
-----
I'll need 3 words:
Word #1 please!
> hi
Word #2 please!
> hi
Word #3 please!
> hi
Shortest: hi
Longest: hi
Average Length: 2.0
"""
#Utkarsh Parasramka
#09/30/2015
#Section : 010

import random
number_of_words = random.randint(3,6)
length_total = 0
longest_word = ''
smallest_word = '    '
print("I'll need", number_of_words, "words:")
for num in range(1,number_of_words+1):
    word = input("Word #" + str(num) + " please!\n>")
    length_word = len(word)
    if length_word <= len(smallest_word):
        smallest_word = word
    if length_word >= len(longest_word):
        longest_word = word
    length_total += length_word
average_length = length_total / number_of_words
print("Shortest:", smallest_word)
print("Longest:", longest_word)
print("Average Length:", average_length)
