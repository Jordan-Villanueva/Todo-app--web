'''
Coding Exercise 1
Define a function that has two parameters, year_of_birth and current_year . The current_year parameter should be a default parameter with the current year as a default value.

The function should calculate and return the age of the user given the year of birth and the current year.

Note: It is enough to define the function for this exercise -no need to call it.

solution:
def age_of_user(user_year_loc, current_year=2023):
    current_age = current_year - user_year_loc
    return current_age

Coding Exercise 2
Your task for this exercise is to use the function you created in exercise 1.
Then, below the function definition, get the year of birth from the user using an input
function and then call and print the defined function to get the user's age as output.
Here is how the program should behave:

solution:
def age_of_user(user_year_loc, current_year=2023):
    current_age = current_year - user_year_loc
    return current_age

birth_year = int(input('Hello. Please enter your birth\'s year: '))
print(f"You are {age_of_user(birth_year)} years old")


Coding Exercise 3
Extend the program you wrote in exercise 2 by printing a message to the user instead of their
 age if their age is greater than 120. Feel free to print any message that you like.

Solution:
def age_of_user(user_year_loc, current_year=2023):
    current_age = current_year - user_year_loc
    return current_age

birth_year = int(input('Hello. Please enter your birth\'s year: '))
age = age_of_user(birth_year)
if age <=120:
    print(age)
else:
    print(f"You are so old... and look like a raisin !!")


Coding Exercise 4
Write a program that gets a list of names from the user and returns the number of names given.
You are encouraged to use a function. Here is how the program would work:

Solution:
def save_on_list(names_loc):
    list_names = names_loc.split(',')
    number = len(list_names)
    return number

string_names = input('Enter names separated by commas (no spaces)')
items = save_on_list(string_names)
print(items)


Coding Exercise 1
Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature.
In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid"
as a string depending on the temperature. The function should be written in a separate file from the
command line interface file. The output should look like in the screenshot below:

    Enter water temperature: -12
    Solid

Let's run it one more time. Here is another example:

    Enter water temperature: 100
    Gas

Note: To check if a value is between two values, you can use
elif 0 < x < 100:

import state_temperature
temp_user = float(input('Enter water temperature: '))
print(funct.state_of_water(temp_user))

Coding Exercise 2
In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants in the script where
 the function is defined. Therefore, your task is to modify the script from exercise 1 by creating two global
 variables/constants in that file, one variable associated with 0 and another associated with 100.
 Then, use those variables in the function instead of the values.

Solution:
import state_temperature as funct
temp_user = float(input('Enter water temperature: '))
print(funct.state_of_water(temp_user))

Modify the function to:
tmax = 100
tmin = 0
def state_of_water(temperature):
    if temperature >= tmax:
        return "Gas"
    elif tmin < temperature < tmax:
        return "Liquid"
    else:
        return "Solid"


Bug-Fixing Exercise 1
The program depicted below consists of two Python files. The program tries to count and print out the number of periods
 in the "Trees are good. Grass is green." . However, running the Home.py file returns an error. Please fix the error.

Home.py:

import functions

nr_of_periods = count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
    return phrase.count('.')

Solution:
change line to nr_of_periods = functions.count


Bug-Fixing Exercise 2
The same program as in exercise 1 now is throwing yet another error. Hunt the error down and fix it.

Home.py:

import functions.py

nr_of_periods = functions.count("Trees are good. Grass is green.")
print(nr_of_periods)


functions.py:

def count(phrase):
    return phrase.count('.')
'''

