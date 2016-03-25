"""
tip.py (6 points)
=====
Create a tip calculator.

1. Print out a nice welcome banner!
2. The program should ask the following:
   a. How many people?	
   b. How much did it cost?
   c. If there are less 6 people, ask: How was the service?  
   d. The values that the service can be are: terrible, poor, ok, good, great
3. If the number of people are greater than or equal to 6, the tip should 
   always be 20%, regardless of service (service should not be asked for if 
   there are greater than 6 people anyway) 
4. Otherwise (less than six people), calculate the tip using the following 
   table:
   * terrible = no tip (0%)
   * poor - 10%
   * ok - 15%
   * good - 20%
   * great - 25%
   * any other input - default to 20% and output a message saying that the
     default tip value will be used
5. Output the calculated tip.
6. Format the number calculated so that there are two decimal places and a
   dollar sign
   
__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name, the date, and your class section at the top of your
  file (above these instructions)

Example Output (consider text after the ">" user input):

Run 1: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 2
How much did it cost? > 25
How was the service (terrible, poor, ok, good, great)? > great
You should probably tip $6.25!

 
Run 2: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 4
How much did it cost? > 70
How was the service (terrible, poor, ok, good, great)? > meh
Couldn't understand meh service; using default 20 percent.
You should probably tip $14.00!

Run 3: 
-----
                    ~~~~~~~
                /// WELCOME \\\
                    ~~~~~~~
 Perhaps I can help you calculate $$$ for yr tip! 

How many people? > 200
How much did it cost? > 950
You should probably tip $190.00!
"""

#Utkarsh Parasramka
#09/29/2015
#Section : 010

print(format("~" * 7, '>29'))
print(format(" // WELCOME \\\ ", '>33'))
print(format("~" * 7, '>29'))
print(" Perhaps I can help you calculate $$$ for yr tip!")
number_of_people = int(input("How many people?\n>"))
cost = float(input("How much did it cost?\n>"))
if number_of_people < 6:
    service = input("How was the service? (terrible, poor, ok, good, great)\n>")
    if service == 'terrible':
        tip = 0 * cost
    elif service == 'poor':
        tip = 0.10 * cost
    elif service == 'ok':
        tip = 0.15 * cost
    elif service == 'good':
        tip = 0.20 * cost
    elif service == 'great':
        tip = 0.25 * cost
elif number_of_people >= 6:
    tip = 0.20 * cost
tip1 = format(tip, '.2f') #I formatted earlier to avoid hassle later
print("You should probably tip $" + tip1)
