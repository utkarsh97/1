"""
worksheet.py - (6 points)
=====

Write the output of the following snippets of code.  First, write your guess in a comment, then try running the code.  Add a comment showing what you actually observed after running the code.  If there's an error,  say there will be an error and propose a fix.

##### Example 1
a = True
b = 25
if b > 25 and a:
    print("Yes!")
else:
    print("No?")

# My guess - Yes!
# Actual output - No?

##### Example 2
a = "7"
if a > 5:
    print("a is greater than five") 

# My guess - Error
# Actual output - Error
# Fix - if int(a) > 5:
"""

##### 1
s = "10"
print(s * 5)

#Answer: 1010101010
#Actual: 1010101010


##### 2
s = "10"
print(s + 5)

#Answer: Error
#Solution: print(int(s)+ 5)


##### 3
quantity = 400
thing = "beverages"
print("I would like " + quantity + " " + thing + ", please.")

#Answer: I would like 400 beverages, please.
#Actual: I would like 400 beverages, please.


##### 4
quantity = 400
thing = "beverages"
print("I would like %s %s, please." % (quantity, thing))

#Answer: I would like 400 beverages, please. 
#Actual: I would like 400 beverages, please.


##### 5
adjective = "sweet "
print("Gimmeh mah %sbeverage" % (adjective * 2))

#Answer: Gimmeh mah sweetsweetbeverage
#Actual: Gimmeh mah sweetsweetbeverage


##### 6
a, b, c = 30, True, False
if (a < 40 or c) and b:
    print("ok!")
else:
    print("whatevs")

#Answer: ok!
#Actual: ok!


##### 7
a, b, c = 30, True, False
if a < 40: 
    d = "hello"
    if d == "world": 
        print("ok!")
    else:
        print("whatevs")
else:
    print("huh?")

#Answer: whatevs
#Answer: whatevs


##### 8
print("foo" != "bar" and 5 > "2")

#Answer: Error
#Solution: print("foo" != "bar" and 5 > 2)


##### 9
print("foo" != "bar" and 5 > 7 % 6 or 2 ** 2 < 4)

#Answer: True
#Actual: True


##### 10
choice = "E"
if choice == "a" or choice == "A":
	print("you chose A")
elif choice == "b" or choice == "B":
	print("you chose B")
elif choice == "c" or choice == "C":
	print("you chose C")
else:
	print("What are *you* talking about???")

#Answer: What are *you* talking about???
#Actual: What are *you* talking about???


##### 11
choice = "B"
if choice == "a" or choice == "A":
	print("you chose A")
elif choice == "b" or choice == "B":
	print("you chose B")
elif choice == "c" or choice == "C":
	print("you chose C")
else:
	print("What are *you* talking about???")

#Answer: you chose B
#Acutal: you chose B


##### 12
if True:
	print("%s jeeooorrb!!!" % ("Gr" + "eat"))

#Answer: Great jeeooorrb!!!
#Actual: Great jeeooorrb!!!
