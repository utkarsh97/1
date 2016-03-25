"""
numbers.py (5 points)
=====
Write a program that outputs the number in the thousands, hundreds, tens and 
ones places of a number. 

1. Create a file called numbers.py
2. Ask the user for a number
3. Calculate the numbers in the thousands, hundreds, tens and ones places
4. Output each place
5. One soution is to use some numeric operators to determine each place 
   (maybe % and // may help)
6. You may have to calculate each place separately
7. Don't worry about input that's not a positive whole number below 10,000

Example Output - Everything after the greater than sign (>) is user input:

Please enter a number
> 256

0 thousands
2 hundreds
5 tens
6 ones
"""

#Utkarsh Parasramka
#21/9/2015
#Section:010

number = int(input("Please enter a number:\n>"))
thousands = number // 1000 #Used the remainder and whole division formula to calculate amounts
number2= number % 1000
hundreds = number2 // 100
number3= number2 % 100
tens = number3 // 10
number4= number3 % 10
ones = number4 // 1
print(thousands, "thousands")
print(hundreds, "hundreds")
print(tens, "tens")
print(ones, "ones")
