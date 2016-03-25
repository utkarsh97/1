"""
is_palindrome.py (4 points)
=====

Determine whether or not a string is a palindrome.

http://en.wikipedia.org/wiki/Palindrome 

For our purposes, strings that are palindromes are strings that are the same 
backwards and forwards.  Some examples of palindromes include:

"racecar"
"straw warts"
"ABBA"

For this assignment, write two functions:

1. reverse(s)
   a. reverses the order of the characters in a string...
   b. takes a string as an argument
   c. returns a new string with the letters of the original reversed
   d. "hello" would return "olleh"
   e. "" returns ""
   f. write at least two assertions for this
2. is_palindrome(s)
   a. determines whether or not the supplied string is a palindrome
   b. takes a string as an argument
   c. returns a boolean value: True if the string is a palindrome, False 
      otherwise
   d. use the above reverse function to help determine whether it is a
      palindrome or not
   e. write at least two asssertions (one for a True case and one for a False
      case)
"""

#Utkarsh Parasramka
#10/26/2015
#Section: 010

def reverse(a):
    word = ''
    for character in a:
        word = character + word
    return word

print("hello")
print(reverse("hello"))
print()
print("baloon")
print(reverse("baloon"))
print()

def is_palindrome(a):
    word = reverse(a)
    if a == word:
        return "True"
    else:
        return "False"

print("racecar")
print(is_palindrome("racecar"))
print()
print("baloon")
print(is_palindrome("baloon"))
