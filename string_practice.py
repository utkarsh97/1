"""
string_practice.py (4 points)
=====
Follow the directions underneath each comment below:
"""

# Part 1 (1 point)
# =======
# Create two strings, "123" and "\n  marshmallows\n  ", assign them to the
# variables, numbers and food, respectively (keep ths spaces and new lines).

numbers = "123"
food = "\n marshmallows\n"

# Use the method that gives back the uppercase version of a string on your
# variable food. Save the result into a variable named result. Print out both
# variables, result and food.

result = food.upper()
print(result)
print(food)

# Part 2 (1 point)
# =======
# Print out the results of calling the methods that do the following:
# * tests if your numbers variable consists of only digits
# * tests if your numbers variable consists of only letters
# * tests if your numbers variable is uppercase (should be false!)
# * tests if your food variable is lowercase

result1 = numbers.isnumeric()
result2 = numbers.isalpha()
result3 = numbers.isupper()
result4 = food.islower()
print(result1)
print(result2)
print(result3)
print(result4)
print()

# Part 3 (1 point)
# =======
# Use the method that gives back the index of a substring from within a
# a larger string to print out the following:
# * call the method to get the index of "mall" in the variable, food... and
#   print out the result
# * call the method again to get the index of "camping" in the variable, food
#   (this should still give back a value, -1!)... and print out the result
#
# Finally use the operator that gives back a boolean if a substring occurs
# within another. Do this to find out of the string "4" is in your string
# variable, numbers.

result5 = food.index("mall")
print(result5)
result6 = food.index("camping")
print(result6)
if "4" in numbers:
    print("True")
else:
    print("False")
print()

# Part 4 (1 point)
# =======
# * print out the result of calling the method that removes white space
#   from the beginning and end of your variable, food
# * print out the result of calling the format method on the string,
#   "{0} agitated ants and {1} anxious antelopes" ... and using the numbers
#   24 and 48 as the variables that get placed inot the placeholders


print("{0} agitated ants and {1} anxious antelopes" .format(24, 48))



