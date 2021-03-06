"""
vet.py (15 points)
=====
This file will contain functions that will help you write a program in 
another file for managing the animals that are coming into a pet clinic.

All animals coming in the clinic have to check in with the following 
information:

* a name ('jane clawston')
* a type / kind ('cat')
* a number representing urgency - 0-100, with the most urgent! (10 - not very 
  urgent)

All of the functions in this file assume that all of the animals that are 
checked-in to the clinic are stored in a specific format - a list of lists. 
Each animal is represented by a 3 element list:

* name will be at index 0
* type will be at index 1
* urgency will be at index 2

For example, a cat named 'jane clawston' that does not have an urgent issue
can be reprsented as:

['jane clawston', 'cat', 10]

Of course, this means that storing all checked-in animals will be a list of 
lists: 
#             animal 1 ------+            animal 2 ------+          animal 3 ------+
#                            |                           |                         |
var animals = [['jane clawston', 'cat', 10], ['franz catka', 'cat', 2], ['bark twain', 'dog', 20]]

Write the following functions AND TEST THEM USING ASSERTIONS.

find_by_name:
-----
Returns the animal with the name specified from a list of animals. 

* parameters: 2 - a string (the name to search for), and a list of animals
* processing:
    1. go through every animal in the list
    2. checks the name
    3. if the name matches the supplied name, give back that animal
* return value: a single animal (a list) or None if the animal is not found

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(find_by_name('gertrude', animal_list))
# will print out ['gertrude', 'goat', 99]


sort_by_name:
-----
This function will return a new list of animals, sorted by the name of the 
the animal (that is, the first element in the list that represents a single 
animal), based on the original list of animals given to the function. The
result will be a new list of animals sorted alphabetically by name.

* parameters: a list of animals (a list of lists)
* processing:
    1. DO NOT USE THE LIST'S SORT METHOD, instead, follow this process
    2. go through every animal in the list positionally (that is, look at the
       first animal, the second, third, etc...)
    3. compare the name of the current animal with the name of the next animal
    4. if the name of the current animal goes after the name of th next animal,
       swap animals
    5. remember, the idiomatic way of swapping in python is a, b = b, a (but
       be careful, as you'll have to swap two elements in a list!)
    6. of course, once you're at the last element, there's no next element to 
       check
    7. once you've gone through all of the animals... REPEAT the whole process
       if you've swapped at least once
    8. stop repeating the process when no swaps occur after going through the
       entire list
    9. here's an example of how it might work:
       element 1: swap with next
       [['zim', 'dog', 10], ['bev', 'dog', 10], ['ari', 'cat', 10]]
       element 2: swap with next
       [['bev', 'dog', 10], ['zim', 'dog', 10], ['ari', 'cat', 10]]
       element 3: last element, do not compare!
       [['bev', 'dog', 10], ['ari', 'cat', 10], ['zim', 'dog', 10]]

       element 1: swap with next
       [['bev', 'dog', 10], ['ari', 'cat', 10], ['zim', 'dog', 10]]
       element 2: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 3: last element, do not compare!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]

       element 1: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 2: do not swap!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]
       element 3: last element, do not compare!
       [['ari', 'cat', 10], ['bev', 'dog', 10], ['zim', 'dog', 10]]

       No swaps occurred... so stop repeating process.

* return value: a list of animals, alphabetically sorted by name

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
sorted_animal_list = sort_by_name(animal_list)
print(sorted_animal_list)
# will print out [['ang', 'unicorn', 50], ['gertrude', 'goat', 99], ['sam', 'snake', 4]]

print_animals:
-----
Prints out the list of animals using their name, kind, and the position they're in 
with in the list (using 1 as the first animal, rather than 0).

* parameters: a list of animals
* processing:
    1. go through every animal in the list
    2. print out the animal's position, name and type
* return value: does not return anything

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
print_animals(animal_list)

prints out...
1 - sam, snake
2 - gertrude, goat
3 - ang, unicorn

get_most_urgent:
-----
This function will find the animal that has the most urgent issue in a list of animals.

* parameters: a list of animals (a list of lists)
* processing:
    1. iterates through entire list of animals
    2. checks the urgency value of each animal
    3. finds the animal with the highest urgency value
    4. if urgency values are the same, choose any animal (it's easiet to
       just choose the last one with the highest value)
* return value: a single animal (a list)

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(get_most_urgent(animal_list))
# will print out ['gertrude', 'goat', 99]

get_least_urgent:
-----
This function will find the animal that has the least urgent issue in a list 
of animals.

* parameters: a list of animals (a list of lists)
* processing:
    1. iterates through entire list of animals
    2. checks the urgency value of each animal
    3. finds the animal with the least urgency value
    4. if urgency values are the same, choose any animal (it's easiet to
       just choose the last one with the least value)
* return value: a single animal (a list)

examples:

animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(get_most_urgent(animal_list))
# will print out ['sam', 'snake', 4]

allowed_animal:
-----
This function will determine whether or not the kind of animal that is 
brought in to the clinic can be treated by the vet.

* parameters: a string, the kind of animal (such as 'dog' or 'alligator')
* processing:
    1. this function will maintain a list of allowed animals
    2. these animals are 'dog', 'cat', 'snake', 'goat', 'pig', 'duck', 
       'narwhale', and 'unicorn'
    2. it will determine if the string passed in, regardless of casing, is
       within the list of allowed animals
* return value: a boolean (True if the animal is allowed, False otherwise)

examples:
    
print(allowed_animal('alligator'))
# False

print(allowed_animal('dog'))
# will print out ['sam', 'snake', 4]
# True
"""

#Utkarsh Parasramka
#11/09/2015
#Section: 010

def find_by_name(name, animal_list):
    name_l = name.lower()
    for animal in animal_list:
        if name_l in animal:
            return animal
    return 'None'
    

'''
animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(find_by_name('gertrude', animal_list))
'''

def sort_by_name(animal_list):
    iteration = 1
    swap = 0
    while iteration > 0:
        for i in range(len(animal_list)):
            if i < len(animal_list) - 1:
                if animal_list[i][0] > animal_list[i+1][0]:
                    animal_list[i], animal_list[i+1] = animal_list[i+1], animal_list[i]
                    swap += 1
                else:
                    swap = 0
        if swap == 0:
            break
        else:
            continue
    return animal_list
'''
animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
sorted_animal_list = sort_by_name(animal_list)
print(sorted_animal_list)
'''

def print_animals(animal_list):
    animals = ''
    for i in range(1, len(animal_list) + 1):
        name = animal_list[i-1][0]
        type_ = animal_list[i-1][1]
        animals += str(i) + ' - ' + name + ', ' + type_ + '\n'
    return animals
'''
animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99], ['ang', 'unicorn', 50]]
print_animals(animal_list)
'''

def get_most_urgent(animal_list):
    most_urgent = [0, 0, -1]
    for i in range(len(animal_list)):
        if animal_list[i][2] >= most_urgent[2]:
            most_urgent = animal_list[i]
    return most_urgent
'''
animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(get_most_urgent(animal_list))
'''

def get_least_urgent(animal_list):
    least_urgent = [0, 0, 101]
    for i in range(len(animal_list)):
        if i < len(animal_list) - 1:
            if animal_list[i][2] <= least_urgent[2]:
                least_urgent = animal_list[i]
    return least_urgent
'''
animal_list = [['sam', 'snake', 4], ['gertrude', 'goat', 99]]
print(get_least_urgent(animal_list))
'''

def allowed_animal(type_of_animal):
    allowed_animals = ['dog', 'cat', 'snake', 'goat', 'pig', 'duck', 'narwhale', 'unicorn']
    type_of_animal_l = type_of_animal.lower()
    if type_of_animal_l in allowed_animals:
        return 'True'
    else:
        return 'False'
'''
print(allowed_animal('alligator'))
print(allowed_animal('dog'))
'''
