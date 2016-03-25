"""
grade.py - 3 points
=====
Translate a numeric grade to a letter grade.
1. Ask the user for a numeric grade.
2. Use the table below to calculate the corresponding letter:
    90-100 - A
    80-89  - B
    70-79  - C
    60-69  - D
     0-59  - F
3. Print out both the number and letter grade.
4. If the value is not numeric, allow the error to happen.
5. However, if the number is not within the ranges specified in the table, output:
    "Could not translate %s into a letter grade" where %s is the numeric grade"

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* including your name, the date, and your class section at the top of your
  file (above these instructions)

Example Output (consider text after the ">" user input):

Run 1:
-----
What grade did you get?
> 59
Number Grade: 59
Letter Grade: F

Run 2:
-----
What grade did you get?
> 89
Number Grade: 89
Letter Grade: B

Run 3:
-----
What grade did you get?
> 90
Number Grade: 90
Letter Grade: A

Run 4:
-----
What grade did you get?
> -12
Couldn't translate -12 into a letter grade

"""

#Utkarsh Parasramka
#09/29/2015
#Section : 010

numeric_grade = int(input("What grade did you get?\n>"))
print("Number Grade:", numeric_grade)
if numeric_grade > 0 and numeric_grade <=59: #I chose and to specify the range of the grade
    print("Letter Grade: F")
elif numeric_grade > 59 and numeric_grade <=69:
    print("Letter Grade: D")
elif numeric_grade > 69 and numeric_grade <=79:
    print("Letter Grade: C")
elif numeric_grade > 79 and numeric_grade <=89:
    print("Letter Grade: B")
elif numeric_grade > 89 and numeric_grade <=100:
    print("Letter Grade: A")
else:
    print("Could not translate", numeric_grade, "into a letter grade.")
