# Coding Exercise 1
# Write a program that asks users to enter a password.
# Then, it checks if the password length is greater than 7 and returns "Great password there!".
'''
Enter a new password: mycool_password3001
Great password there !

If the password has 7 or fewer characters, the program returns, "YOur password is weak".
Enter a password: 1234
Your password is weak

solution:
password = input('Enter a new password: ')
password = password.strip()

if len(password) >7:
    print('Great password there !')
else:
    print('Your password is weak')

Coding Exercise 2
Extend the program we built in Coding Exercise 1 by adding a new feature.
The new feature should allow the program to return "Password is OK, but not too strong"
when the password is exactly seven characters long.

Enter a new password: 1234567
Password is OK, but not too strong

Solution:
password = input('Enter a new password: ')
password = password.strip()

if len(password) >7:
    print('Great password there !')
elif len(password) == 7:
    print('Password is OK, but not too strong')
else:
    print('Your password is weak')


Bug-Fixing Exercise 1: The program below intends to find out how many items have at least one underscore ("_") character in them.  However, there is an error with the code. Try to find and fix it.

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
if '_' in id:
    x = x + 1
print(x)

solution:
    indent the if statement

Bug-Fixing Exercise 2: This program also intends to find out how many items have an underscore in them. However, the program has a bug. It doesn't return an error message, but it returns:
1
1
2
Instead, the expected output is:
2

Try to fix the program so it returns the expected output. Here is the buggy program:
ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x = x + 1
    print(x)

solution:
unindent print statement

Bug-Fixing Exercise 3: Fix the program below so it prints out "OK" when the perimeter is less than 14 and the area is less than 8.

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area > 10:
    print("OK")
else:
    print("NOT OK")

solution:
change area < 8

Coding Exercise 1
Build a percentage calculator that gets from the user the "total value" and the "value" and returns the percentage as shown below:
Enter total volume: 50
Enter value: 20
That is 40.0%

The program should also print a message if the user doesn't enter a number for the "total value or
for the "value":
Enter total value: 20
Enter value: hi
You need to enter a number. Run the program again.

solution:
try:
    volume = float(input('Enter total volume: '))
    value = float(input('Enter value: '))
    percentage = value*100/volume
    print('That is ',percentage)
except ValueError:
    print('You need to enter a nunber. Run the program again.')


Coding Exercise 2
As you might know, it is not mathematically possible to divide a number by zero.
Consequently, this is also not possible in Python either -you will get a ZeroDivisionError if you try:

# >>> 20 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
With that in mind, your task for this exercise is to extend the program you created in Exercise 1
by displaying a message to the user when they enter 0 for the "total value".

Enter total value: 0
Enter value: 20
Your total value cannot be zero

solution:
try:
    volume = float(input('Enter total volume: '))
    value = float(input('Enter value: '))
    percentage = value*100/volume
    print('That is ',percentage)
except ValueError:
    print('You need to enter a nunber. Run the program again.')
except ZeroDivisionError:
    print('Your total value cannot be zero')



Bug-Fixing Exercise 1
Have a look at the program below:

waiting_list = ["john", "marry"]
name = input("Enter name: ")
number = waiting_list.index(name)
print(f"{name}'s turn is {number}")

When the user enters the name of one of the waiting_list members, the program returns the index of
that name. For example, when the user enters "john", 0 is printed out.

Enter name: john
john's turn is 0

If the user enters a name that is not in the list, such as "zen", the program throws an error.
Enter name: zen

ValueError: 'zen' is not in list
Change the program, so it prints out "zen is not in the list" instead of returning an error when
the user enters "zen" or any other name that is not in the list.

solution:
try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    print(f"'{name}' is not in list")


Coding Exercise 1
The code below is incomplete. It should calculate and print out the maximum value of the grades list. Please complete
the function and then call it.

def get_max():
    grades = [9.6, 9.2, 9.7]
The output of your code should be:

9.7

Hint: You can use the max(list) function to find the maximal value of a list.
solution:
def get_max():
    grades = [9.6, 9.2, 9.7]
    local_max = max(grades)
    return local_max
print(get_max())

Coding Exercise 2
The function we wrote in exercise 1 returned 9.7.  Change the function so this time it returns Max: 9.7,
Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.

solution:
def get_max():
    grades = [9.6, 9.2, 9.7]
    local_max = max(grades)
    local_min = min(grades)
    return local_max, local_min

max, min = get_max()
print(f"Max: {max}, Min: {min}")


Bug-Fixing Exercise 1
The following get_maximum function is designed to return the maximum value of the celsius list,
while the last two lines of the code will convert the celsius value to Fahrenheit and print it out.

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    print(maximum)

celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
However, when running the code, the following error is generated:

TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'

Try to fix the problem so that the last two lines can correctly get the maximal celsius value from the function definition
and convert that value to Fahrenheit.

solution:
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum

celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32
print(fahrenheit)


'''

