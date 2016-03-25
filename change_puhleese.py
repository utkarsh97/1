"""
change_puhleese.py (15 points) (1 point extra credit)
=====
You're the manager of a tiny boutique that sells Python related gifts and 
knick-knacks (like plush Python stuffed animals, Guido Van Rossum bobble head
dolls, etc. ). Unfortunately, you don't have any paper bills on hand, you only 
have coins! 

To help you calculate change, you reprogram you cash register to print out the 
exact change that's needed, broken down by quarters, dimes, nickels and pennies.

Here's what your program should do:

1. Ask the cashier for information regarding the items purchased. It will 
   assume that everyone buys exactly three items (!?). For every item:
   a. ask for name of the item
   b. ask for the price (assume that users will always enter a number with a 
      decimal point)
   c. ask for quantity (assume that users will always enter a whole number)
2. Ask the cashier for how much the user paid. Assume that the amount paid
   is at least as much as the total owed (including sales tax)
3. Print out a receipt that contains the following information:
   a. name, price, quantity and total cost per item purchased
   b. the total cost of all of the items
   c. the sales tax based on the cost of all of the items - sales tax in the
      city is 8.875%
   d. the total amount owed, including salestax
   e. the total amount paid
   f. the change owed, followed by a break down of how many quarters, dimes, 
      nickels and pennies will be given back
      * it will always print out the number of coins for each denomination, 
        even if the quantity is 0
   g. __IT IS OK IF SOME OF YOUR CALCULATIONS ARE OFF BY 1 CENT__
4. The receipt should be in the following format:
   a. the width of the receipt is 80 characters long total
   b. it has a center aligned title: PREMIER PYTHON PLAZA RECEIPT
   c. followed by a line created by equal signs that's 80 characters long (===)
      * __DO NOT TYPE OUT__ 80 ='s ... use what we learned about Python types,
        operators, etc. to do this
   d. print out the costs per item...
   e. print out another line created by equal signs
   f. print out the calculations for total item cost, sales tax, etc.
   g. print out another line created by equal signs
   h. print out the number of quarters, dimes, etc.
   i. "headings" in a line are left justified: item name x quantity ... cost
   j. prices / costs:
      * are right justified
      * have a dollar sign
      * have two decimal places
      * hint: you may have to use format more than once to get the decimal
        places... but then you'll need to add a dollar and format again!
   k. assume that all item names and costs are less than 40 characters long
   l. see the sample interaction below
      * everything after the > (greater than sign) is user input
      * the receipt is at the end
      * __YOUR OUTPUT SHOULD MATCH THE OUTPUT BELOW!__
5. __COMMENT YOUR SOURCE CODE__ by 
   a. briefly describing sections of your program (for example "# calculates the number of quarters, dimes, nickels and pennies" could go above the part of your code that runs those calculations). 
   b. include your name, the date, and your class section at top of your file (above everything else)

What is the name of the first item?
> Guido Van Rossum Bobble Head
How much does the first item cost?
> 10
How many are being purchased?
> 3
What is the name of the second item?
> Python Stuffed Animal
How much does the second item cost?
> 29.99
How many are being purchased?
> 1
What is the name of the third item?
> Hello World T-Shirt
How much does the third item cost?
> 12.50
How many are being purchased?
> 3
How much was paid?
> 150.03
....
4388
175
<class 'int'>
                          PREMIER PYTHON PLAZA RECEIPT
================================================================================
3 x Guido Van Rossum Bobble Head                                          $30.00
1 x Python Stuffed Animal                                                 $29.99
3 x Hello World T-Shirt                                                   $37.50
================================================================================
TOTAL COST OF ITEMS                                                       $97.49
SALES TAX                                                                  $8.65
AMOUNT OWED                                                              $106.14
AMOUNT PAID                                                              $150.03
CHANGE                                                                    $43.89
================================================================================
CHANGE:
175 x quarters
1 x dimes
0 x nickels
4 x pennies



EXTRA CREDIT 
=====

* __USE CALCULATIONS TO DETERMINE MANY SPACES__ to pad your title with (do not 
  just write out space characters manually)
* you can use the built-in function, len to get the length of a string
* len("hello") --> 5
* remember that the 2nd parameter to the format function is a string that 
  determines how a string is formatted
* can you construct that string dynamically with the length of the title?
"""
#Utkarsh Parasramka
#21/9/2015
#Section:010

#Extra Credit Work Included in the Program
name1 = input("What is the name of the first item?\n>")
price1 = float(input("How much does the first item cost?\n>"))
number1 = int(input("How many are being purchased?\n>"))
name2 = input("What is the name of the second item?\n>")
price2 = float(input("How much does the second item cost?\n>"))
number2 = int(input("How many are being purchased?\n>"))
name3 = input("What is the name of the third item?\n>")
price3 = float(input("How much does the third item cost?\n>"))
number3 = int(input("How many are being purchased?\n>"))
amount_paid = float(input("How much was paid?\n>"))
total1 = price1 * number1
total2 = price2 * number2
total3 = price3 * number3
total_cost = total1 + total2 + total3
sales_tax = 8.875/100 * total_cost
amount_owed = total_cost + sales_tax
change = amount_paid - amount_owed
formatted_total_cost = format(total_cost, '.2f')
formatted_sales_tax = format(sales_tax, '.2f')
formatted_change = format(change, '.2f')
formatted_amount_paid = format(amount_paid, '.2f')
formatted_amount_owed = format(amount_owed, '.2f')
formatted_total1 = format(total1, '.2f')
formatted_total2 = format(total2, '.2f')
formatted_total3 = format(total3, '.2f')
title = input("What is the title for the receipt?\n>") #Any Title works
length = int(len(title))
length1 = int(input("What is the length of the receipt?\n>")) #Any reasonable length of the receipt can be printed
space = (length1 - length)/2 #Formula used to centre the title
padding = int(space + length) #Formula used to centre the title
length2 = int((length1)/2) #Formula to left justify names of items and subtitles
length3 = int(length2 - 1) #Formula to right justify amounts
print(format(title, '>' + str(padding)))
print("=" * length1)
print(format(str(number1) + " x " + name1, '<' + str(length2)), format("$" + formatted_total1, '>' + str(length3))) #I used the length of the receipt to justify names and amounts accordingly
print(format(str(number2) + " x " + name2, '<' + str(length2)), format("$" + formatted_total2, '>' + str(length3)))
print(format(str(number3) + " x " + name3, '<' + str(length2)), format("$" + formatted_total3, '>' + str(length3)))
print("=" * length1)
print(format("TOTAL COST", '<' + str(length2)), format("$" + formatted_total_cost, '>' + str(length3)))
print(format("SALES TAX", '<' + str(length2)), format("$" + formatted_sales_tax, '>' + str(length3)))
print(format("AMOUNT OWED", '<' + str(length2)), format("$" + formatted_amount_owed, '>' + str(length3)))
print(format("AMOUNT PAID", '<' + str(length2)), format("$" + formatted_amount_paid, '>' + str(length3)))
print(format("CHANGE", '<' + str(length2)), format("$" + formatted_change, '>' + str(length3)))
print("=" * length1)
print("CHANGE:")
quarters = change // 0.25 #Calculating number of coins
change1 = change % .25
dimes = change1 // 0.10 
change2 = change1 % 0.10
nickels = change2 // 0.05 
change3 = change2 % 0.05
pennies = change3 // 0.01 
print(int(quarters), "x quarters")
print(int(dimes), "x dimes")
print(int(nickels), "x nickels")
print(int(pennies), "x pennies")
