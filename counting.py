"""
counting.py - 2 points
=====

use *while* loops to do the following:

* print out "while loops"
* use a while loop to count from 2 up-to and including 10 by 2's.
* use another while loop to count down from 5 down to 1


use *for* loops to do the following:

* print out "for loops"
* use a for loop to count from 2 up-to and including 10 by 2's.
* use another for loop to count from 5 down to 1.

* comment your code (name, date and section on top, along with appropriate 
  comments in the body of your program)

example output:

while loops
2
4
6
8
10
5
4
3
2
1
for loops
2
4
6
8
10
5
4
3
2
1
"""
#Utkarsh Parasramka
#09/30/2015
#Section : 010

number = 0
print("while loops")
while number < 10:
    number += 2
    print(number)
number_1 = 6
while number_1 > 1:
    number_1 -= 1
    print(number_1)
print("for loops")
for num in range(2,11,2):
    print(num)
for num_1 in range(5,0,-1):
    print(num_1)
