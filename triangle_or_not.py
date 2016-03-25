"""
triangle_or_not.py - (6 points)
=====
Ask the user for 3 points on the coordinate plane. Calculate the distances
between each comination of points (that is, the length of each potential side
of a triangle), and use those calculations to determine whether or not the
points make a valid triangle.

1. Ask the user for the x and y coordinates of 3 points, for example:
   Enter point #1 x:
   * assume that all inputs are ints
   * you do not have to do any input validation
2. Calculate and output the length of each side (the distances between each
   points).
   * You can assume that Side #1 is composed of points 1 and 2, Side #2 is 2
     and 3, and Side #3 is 3 and 1
   * Look up the distance forumla; it involves square root. __YOU MUST USE THE
     MATH MODULE'S__ sqrt function to do this: math.sqrt(100) -> 10 (remember
     to import math first)
   * Output the length of each side: Side #1: <value>
3. Finally, determine if the points create a valid triangle...
   * Side #1 + Side #2 must be longer than Side 3
   * Side #2 + Side #3 must be longer than Side 1
   * Side #3 + Side #1 must be longer than Side 2
   * Output whether or nota valid triangle is formed:
     a. YOU HAZ TRIANGLE
     b. Nope, not a triangle.

Example Interaction 1:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 100
Enter point #2 y: 0
Enter point #3 x: 50
Enter point #3 y: 2
Side #1     100.00
Side #2      50.04
Side #3      50.04
YOU HAZ TRIANGLE

Example Interaction 2:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 10
Enter point #2 y: 10
Enter point #3 x: 1
Enter point #3 y: 0
Side #1      14.14
Side #2      13.45
Side #3       1.00
YOU HAZ TRIANGLE

Example Interaction 3:
-----
Enter point #1 x: 0
Enter point #1 y: 0
Enter point #2 x: 50
Enter point #2 y: 50
Enter point #3 x: 100
Enter point #3 y: 100
Side #1      70.71
Side #2      70.71
Side #3     141.42
Nope, not a triangle
"""

#Utkarsh Parasramka
#09/25/2015
#Section : 010

point1_x = int(input("Enter point #1 x:"))
point1_y = int(input("Enter point #1 y:"))
point2_x = int(input("Enter point #2 x:"))
point2_y = int(input("Enter point #2 y:"))
point3_x = int(input("Enter point #3 x:"))
point3_y = int(input("Enter point #3 y:"))
import math
difference_side1_y = point2_y - point1_y 
difference_side1_x = point2_x - point1_x
total_of_squares_1 = difference_side1_y ** 2 + difference_side1_x ** 2 #putting distance formula without square-root
side1 = math.sqrt(total_of_squares_1) #using math import to square-root
difference_side2_y = point3_y - point2_y
difference_side2_x = point3_x - point2_x
total_of_squares_2 = difference_side2_y ** 2 + difference_side2_x ** 2
side2 = math.sqrt(total_of_squares_2)
difference_side3_y = point1_y - point3_y
difference_side3_x = point1_x - point3_x
total_of_squares_3 = difference_side3_y ** 2 + difference_side3_x ** 2
side3 = math.sqrt(total_of_squares_3)
print("Side #1 :", format(side1, '.2f')) #formatting to 2 decimal places for convenience
print("Side #2 :", format(side2, '.2f'))
print("Side #3 :", format(side3, '.2f'))
total1 = side1 + side2
total2 = side2 + side3
total3 = side3 + side1
if total1 > side3 and total2 > side1 and total3 > side2: #using 'and', since all must be satisfied
    print("YOU HAZ A TRIANGLE!")
else:
    print("Nope, not a triangle.")
