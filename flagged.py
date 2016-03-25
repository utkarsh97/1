"""
flagged.py - 7 points
=====
Create a program that generates a pattern for a flag.

* ask the user for a width of the flag
    * the width should be greater than 0
    * if it isn't, ask again until the user enters a valid value
* then... ask the user for a character
    * the character can be any character except empty string
    * it can even be multiple characters!
    * if it's an empty string, ask again until the user enters a valid 
      character
* construct a flag based on the input (notice the relationship between the
  width and the number of times the character appears horizontally below)
    * hint: string format, string repetition, and/or len may help
    * hint: the spaces in the interior must take the number of characters
      in the "character" input into account!
* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

Run 1 (invalid width, ask again):
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> -1
Let's try that again, but this time with something less negative.
What's the width of your flag?
...

Run 2 (invalid character, empty response, ask again):
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 5
What character(s) do you want to use?
>
Let's try that again, but this time with maybe more character(s).
What character(s) do you want to use?
>

Run 3 (money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 5
What character(s) do you want to use?
> $
$$$$$
 $$$$
  $$$
   $$
    $
   $$
  $$$
 $$$$
$$$$$

Run 3 (less money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 4
What character(s) do you want to use?
> $
$$$$
 $$$
  $$
   $
  $$
 $$$
$$$$

Run 4 (ugh, even less money flag!)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 1
What character(s) do you want to use?
> $
$

Run 5 (character has multiple characters in it)
-----
Hi, I'm flaggy the flagmaker. Let's make a flag.
What's the width of your flag?
> 3
What character(s) do you want to use?
> --o
--o--o--o
   --o--o
      --o
   --o--o
--o--o--o
"""

#Utkarsh Parasramka
#10/05/2015
#Section: 010

print("Hi, I'm flaggy the flagmaker. Let's make a flag.")
width = int(input("What's the width of your flag?\n>"))
while width <= 0:
    print("Let's try that again, but this time with something less negative.")
    width = int(input("What's the width of your flag?\n>"))
if width > 0:
    character = input("What character(s) do you want to use?\n>")
    while character == '':
        print("Let's try that again, but this time with maybe more character(s).")
        character = input("What character(s) do you want to use?\n>")
    length_ch = int(len(character))
    if length_ch > 0:
        width_flag = length_ch * width #determining width of flag using characters
        for num in range(width,0,-1):
            print(format(character * num, '>' + str(width_flag)))
        for num_1 in range(2,width+1):
            print(format(character * num_1, '>' + str(width_flag)))
