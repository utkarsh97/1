"""
You have a file called zips.txt

11211|10012|11364|10457|NY
06927|06532|CT
08720|07470|07030|NJ
15042|15043|15044|15046|PA
19970|DE

Write a program that:

* reads in zips.txt
* asks for a state abbreviation by displaying the possible state abbreviations
  that can be entered (based on the contents of the file)
* and, depending on the user input...
    * will print out the zip codes for that state __in order__
    * or print out "I don't know that state" if the input doesn't match

Example Interaction 1:
-----

Please enter a state (your options are NY,CT,NJ,PA,DE)
> CT

The zip codes for CT are:

06532
06927

Example Interaction 2:
-----

Please enter a state (your options are NY,CT,NJ,PA,DE)
> CA

I don't know that state.

"""

#Utkarsh Parasramka
#12/10/2015
#Section: 010

zip_codes = open("zips.txt", "r")
zips = zip_codes.read()
zips_ = zips.strip()
all_states = zips_.split('\n')
entire_list = []
for item in all_states:
    all_codes = item.split('|')
    entire_list.append(all_codes)
answer = input("Please enter a state (your options are NY,CT,NJ,PA,DE)\n>")
state = answer.upper()
codes = []
for item in entire_list:
    if state in item:
        codes = item[:len(item)-1]
        codes.sort()
        print("The zip codes for", state, "are:\n")
        for code in codes:
            print(code)
if codes == []:
    print("I don't know the state.")
