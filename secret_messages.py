"""
secret_messages.py (15 points + 3 points extra credit)
=====

Write a program that encrypts a message (encodes a message so that it's 
"secret") by shifting every letter in the message a number of spaces to the
left or right. This simple encryption technique is called a Caesar Cipher:

https://en.wikipedia.org/wiki/Caesar_cipher

For example, shifting by three maps the original letters of a message to a 
letter 3 places to the right from the original letter. If there are no more 
letters to the right, continue by going back to the beginning of the alphabet. 
For a shift of three, the letters would be mapped as follows:

A → D
B → E
C → F
.
.
.
Y → B
Z → C

So... encrypting the message "ABC" would yield "DEF". A few more examples:

"Hello There" → "Khoor Wkhuh"
"Oxen and Zebra" → "Rahq dqg Cheud"

In our implementation of Casear's Cipher:

* IF A SHIFTED LETTER GOES BEYOND 'Z' or 'z', continue counting places from
  the left (that is, go back to A, and continue your shift from there)
* DO NOT SHIFT ANY CHARACTER THAT'S NOT A LETTER (retain punctuation, spaces, 
  etc.): ... with a shift of 10, "a!  b!  c!" → "k!  l!  m!"
* CASING (upper/lower case) SHOULD BE PRESERVED: shift by 1, "aRe" → "bSf"

To write this program, create 3 functions:

* encrypt - encrypt a string using Caesar's Cipher
    * input: a string to encrypt and the number of letters to shift
    * processing: use Caesar's Cipher to encrypt the string passed in based
      on the specified shift value
    * output: returns a string
* decrypt - decrypt a string using Caesar's Cipher
    * input: a string to decrypt and the number of letters that the original 
      message was shifted
    * processing: use Caesar's Cipher to decrypt the string passed in assuming
      that the original shift is the shift value passed in
    * output: returns a string
* main - contains the main logic of your program
    * input: none
    * processing: continually asks the user for input... (see specifications
      below)
    * output: does not return anything
    * remember to call main at the end of your program!

The program will:

* continually ask "(e)ncrypt, (d)ecrypt or (q)uit?" until the user enters q 
  to quit
* it should accept both upper and lowercase versions of e, d, and q
* if the user chooses encrypt
    * ask the user for a message... and how many letters to shift by
    * display the encrypted message
* if the user chooses decrypt
    * ask the user for a message... and how many letters the original message
      was shifted by
    * display the decrypted message
* hint: one way to solve this is to use chr and ord
    * what are the unicode code points of boundaries of letters?
    * check out the following chart:
      http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec
    * remember that the boundaries differ for upper and lowercase letters

Example output below:
-----

(e)ncrypt, (d)ecrypt or (q)uit?
> ???
Sorry, I can only (e)ncrypt, (d)ecrypt or (q)uit...
(e)ncrypt, (d)ecrypt or (q)uit?
> e
How many places should each letter be shifted?
> 3
What is the message?
> Hello There
Khoor Wkhuh
(e)ncrypt, (d)ecrypt or (q)uit?
> d
How many places was each letter shifted?
> 3
What was the message?
> Vhfuhw
Secret
(e)ncrypt, (d)ecrypt or (q)uit?
> e
How many places should each letter be shifted?
> -1
What is the message?
> bcd
abc
(e)ncrypt, (d)ecrypt or (q)uit?
> q
Bye!

As always, comment your code, including your name, date and section at the top
of the file.

Extra Credit (3 points)
-----
Your encrypt functions probably look very similar. Try moving out the common
code into another function that both encrypt and decrypt call.

If you do the extra credit PLEASE LEAVE THE GRADER FEEDBACK SAYING THAT YOU
ATTEMPTED THE EXTRA CREDIT.
"""

#Utkarsh Parasramka
#10/26/2015
#Section: 010

def Caesar_Cipher(a, b, c): # Extra Credit
    word = ''
    for character in a:
        ord_ = ord(character)
        if ord_ >= 97 and ord_ <= 122 or ord_ >= 65 and ord_ <= 90:
            if c == 'e':
                ord_new = ord_ + b
                if ord_new > 122:
                    ord_new = ord_new - 26
                elif ord_new > 90 and ord_new < 97:
                    ord_new = ord_new - 26
                word += chr(ord_new)
            elif c == 'd':
                ord_new = ord_ - b
                if ord_new < 65:
                    ord_new = ord_new + 26
                elif ord_new < 97 and ord_new > 90:
                    ord_new = ord_new + 26
                word += chr(ord_new)
            else:
                word += character
        return word

program = ''
while program != 'e' and program != 'd' and program != 'q':
    program_ = input("(e)ncrypt, (d)ecrypt or (q)uit?\n>")
    program = program_.lower()
    if program == 'e':
        places= int(input("How many places should each letter be shifted?\n>"))
        word = input("What is the message?\n>")
        print(Caesar_Cipher(word, places, 'e'))
    elif program == 'd':
        places= int(input("How many places should each letter be shifted?\n>"))
        word = input("What is the message?\n>")
        print(Caesar_Cipher(word, places, 'd'))
    elif program == 'q':
        print("Bye!")
        break
    elif program != 'e' or program != 'd' or program != 'q':
        print("Sorry, I can only (e)ncrypt, (d)ecrypt or (q)uit...")

