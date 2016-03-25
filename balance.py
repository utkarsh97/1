"""
balance.py (6 points)
=====

One tedious aspect of programming is keeping track of opened and closed 
parentheses.  Every open parentheses needs a corresponding closing parentheses.  
If the parentheses are all correctly opened and closed, then the parentheses 
are *balanced*.  Wouldn't it be great if we had some tool to let us know
if our parentheses are balanced?

You can write one (though, IDLE already does this)!  Write a function that 
determines whether or not a series of open and closed parentheses are balanced. 
DO NOT JUST COUNT the number of left and right parentheses and check if they're 
equal! This will not work becuase order matters.

1. Create a function called balanced_parentheses
2. It should take one argument, a string of opened and closed parentheses
3. It should return True or False depending on whether or not all opened
   parentheses have a corresponding close, and are in the *proper order*!
4. Write assertions for each of the examples below
5. AGAIN, DO NOT COUNT THE NUMBER OF OPEN AND CLOSED PARENTHESES AND COMPARE
   (use the algorithm below)

Pseudocode:
Start with an empty list to temporarily store open parentheses
Go through every character in the string
    If you see an open parentheses add it to the list
    But if you see a close parentheses, remove the last open from your list
    If there's no open to remove... uh-oh! Not balanced!
If there are still open parentheses at the end of your list, not balanced!

* hint: Nested if statements may be useful
* hint: The pop method may be useful (or slicing may work too)

Examples: 
-----
# all return True
print(balanced_parentheses('(()()()())'))
print(balanced_parentheses('(((())))'))
print(balanced_parentheses('(()((())()))'))

# all return False
print(balanced_parentheses(')('))
print(balanced_parentheses('((((((())'))
print(balanced_parentheses('()))'))
print(balanced_parentheses('((((((())'))
print(balanced_parentheses(')(()'))
print(balanced_parentheses('())('))

"""

#Utkarsh Parasramka
#11/09/2015
#Section: 010

def balanced_parentheses(my_string):
    my_list = []
    for character in my_string:
        if ord(character) == 40:
            my_list.append('(')
        elif ord(character) == 41:
            if len(my_list) > 0:
                my_list.remove('(')
            else:
                return 'False'
    if len(my_list) == 0:
        return 'True'
    elif len(my_list) > 0:
        return 'False'

# all return True
print(balanced_parentheses('(()()()())'))
print(balanced_parentheses('(((())))'))
print(balanced_parentheses('(()((())()))'))

# all return False
print(balanced_parentheses(')('))
print(balanced_parentheses('((((((())'))
print(balanced_parentheses('()))'))
print(balanced_parentheses('((((((())'))
print(balanced_parentheses(')(()'))
print(balanced_parentheses('())('))
