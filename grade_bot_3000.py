"""
grade_bot_3000.py (7 points)
=====
You've been hired as a grader for several classes, and the total number of 
students you have to grade are over a 1000 (ughhh). Calculating grades by hand for all of those students would drive you INSANE. ... So you create a robot to do it 
for you. A robot in Python. That grades stuff.

And you call it: ~~~GRADE BOT 3K~~~

Your robot will:

1. ask the student for their name
2. greet the student and ask for what class they're in ("Hi ... <student name>, 
   what class are you in?")
3. ask the student how much tests are worth in the class
4. ask for 2 test scores
5. calculate the average for tests and print it out (keep 2 decimal places and
   add a percent sign)
6. ask the student how much homework is worth in the class
7. ask for 2 homework scores
8. calculate the average for homework and print it out (keep 2 decimal places and
   add a percent sign)
9. calculate their final grade based on the weights provided and output it (again
   keep 2 decimals, use a percent sign, and mention the class name)

Example Interaction
-----
Hi there. I'm Grade Bot 3K. What's your name?
> Joe
Hi Joe. What class are you in?
> Intro to Robot Making
What percent are tests worth in your class?
> 70
What was your score for test 1?
> 89
What was your score for test 2?
> 73
Your test average is: 81.00%
What percent are homeworks worth in your class?
> 30
What was your score for hw 1?
> 95
What was your score for hw 2?
> 99
Your hw average is: 97.00%
Your final grade for the Intro to Robot Making is 85.80%

__COMMENT YOUR SOURCE CODE__ by 

* briefly describing parts of your program 
* include your name, the date, and your class section at top of your file (above 
  everything else)

"""

#Utkarsh Parasramka
#21/9/2015
#Section:010

name = input("Hi, I'm Grade Bot 3000. What's your name?\n>")
course = input("Hi " + name + ". What class are you in?\n>")
test_percent = input("What percent are tests worth in your class?\n>")
test1 = input("What was your score on test 1?\n>")
test2 = input("What was your score on test 2?\n>")
average_test = (float(test1) + float(test2))/2
print("Your test average is:", format(average_test, '.2f') + "%")
hw_percent = input("What percent are homeworks worth in your class?\n>")
hw1 = input("What was your score for homework 1?\n>")
hw2 = input("What was your score for homework 2?\n>")
average_hw = (float(hw1) + float(hw2))/2
print("Your homework average is:", format(float(average_hw), '.2f') + "%")
final_grade = (float(test_percent) * average_test)/100 + (float(hw_percent) * average_hw)/100 #Used weightage formula to calculate final grade
print("Your final grade for the", course, "is:", format(final_grade, '.2f') + "%")
