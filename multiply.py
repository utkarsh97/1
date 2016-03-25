"""
multiply.py (3 points)
=====
Write a program that:

* asks the user for a number
* prints out a table of that number multiplied by the first 7 prime numbers:  
  2, 3, 5, 7, 11, 13, 17
* it will format the output so that the original number and the prime number are
  left aligned
* the product is right aligned
  * when using format, don't change the width to align the product
  * keep the width constant
* __COMMENT YOUR SOURCE CODE__ by 
   * briefly describing parts of your program 
   * include your name, the date, and your class section at top of your file 
     (above everything else)

Example interaction (everything after > is user input):
-----
Give me a number
> 17
17 * 2             34
17 * 3             51
17 * 5             85
17 * 7            119
17 * 11           187
17 * 13           221
17 * 17           289
"""

#Utkarsh Parasramka
#21/9/2015
#Section:010

number=int(input("Give me a number\n>"))
number2= number * 2
number3= number * 3
number5= number * 5
number7= number * 7
number11= number * 11
number13= number * 13
number17= number * 17
print(number, format("* 2", "<15"), number2) #Basic formatting to right justify multiples
print(number, format("* 3", "<15"), number3)
print(number, format("* 5", "<15"), number5)
print(number, format("* 7", "<15"), number7)
print(number, format("* 11", "<15"), number11)
print(number, format("* 15", "<15"), number13)
print(number, format("* 17", "<15"), number17)

