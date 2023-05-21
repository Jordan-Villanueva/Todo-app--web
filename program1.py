'''
Welcome to your first set of coding exercises!
-----------------------------------------------------------------------------------------------
Coding Exercise 1
Write a Python program following the steps below:

1. Create a variable (any name) and store a string in the variable.

2. Then, print out the type of the variable.

Note: You are expected to work on PyCharm (or another IDE) to code your solution. You can code each exercise in a separate .py file. When you're finished, compare your code to the instructor's, which is provided in the link below.

var = "Amigos"
print(type(var))
-----------------------------------------------------------------------------------------------
Coding Exercise 2

Write a Python program that gets input from the user and prints out that input.

print(input("Give me some input:"))
-----------------------------------------------------------------------------------------------
Bug-Fixing Exercise 1
The following code has a syntax error. Try to fix it.

answers = ['Yes', 'No', 'Yes', 'No', 'No'

answers = ['Yes', 'No', 'Yes', 'No', 'No']
-----------------------------------------------------------------------------------------------
Bug-Fixing Exercise 2
The following code throws an error. Try to fix it.

my_answer = input("What is your answer?")
answers = ['Yes', 'No', 'Yes' 'No' my_answer]

answers = ['Yes', 'No', 'Yes', 'No', my_answer]

-----------------------------------------------------------------------------------------------
Bug-Fixing Exercise 3
The following code has an error. Try to fix it.

my_answer = input(What is your answer?)
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
my_answer = input("What is your answer?")
-----------------------------------------------------------------------------------------------
Bug-Fixing Exercise 4
The following code throws an error. Try to fix it.

my_answer = input["What is your answer?"]
answers = ['Yes', 'No', 'Yes', 'No', my_answer]
my_answer = input("What is your answer?")


Create a program that prompts the user to input their name once. Then, the program prints out the name once with the first letter capitalized.
name = input("What is your name? ")
print(name.capitalize())

Create a program that prompts the user to input their name once. Then, the program repeatedly prints out the name with the first letter capitalized.
name = input("What is your name? ")
while(True)
    print(name.capitalize())


The code below has two bugs. Hunt them down and fix them.
    while True
    print("Hello") --- agregar indentacion y dos puntos


The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:

greeting = "hello"
print(upper(greeting))
However, the program returns an error. Can you help fix the code, so it prints out HELLO?

Respuesta:
greeting = "hello"
print(greeting.upper())


A programmer wrote the following program:

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
print(countries)
The expected output is as follows:
Enter the country: Cambodia
['Cambodia']
Enter the country: Triomindia
['Cambodia', 'Triomindia']
Enter the country:

Solucion

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)


Coding Exercise 1
Create a program that does the following:

1. Prompts the user to input the country they are from.

2. If the user enters the word USA, the program prints out Hello.

3. If the user enters the word  India, the program prints out Namaste.

4. If the user enters the word Germany, the program prints out Hallo.

Note: Strings are case-sensitive in Python, meaning germany and Germany are treated as two different strings.

country = input("Where are you from?")
country.strip()
country.capitalize()

match country:
    case 'USA':
        print("Hello")
    case 'India':
        print("Namaste")
    case 'Germany':
        print("Hallo")
    case whatever:
        print("I don't have an answer for you")
        break


Coding Exercise 2
ingredients = ["john smith", "sen plakay", "dora ngacely"]
Copy-paste the above line into your IDE and write a for-loop below that line that makes the program produce the following output:
John Smith
Sen Plakay
Dora Ngacely

for a in ingredients:
    print(a.title())

Bug-Fixing Exercise 1
The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized. However, the programmer has done something wrong. Try to find and fix the issue.

for i in buttons:
    print(i.capitalize())

buttons = ["cancel", "reply", "submit"]

solution: declare buttons first

Bug-Fixing Exercise 2
The programmer is again missing something in the code. Try to find what it is and fix it.

buttons = ["cancel", "reply", "submit"]

for i in buttons:
print(i.capitalize())

solution: indentation inside for loop

Bug-Fixing Exercise 3
The code below is supposed to print out the items of the list with the first character of each item capitalized. However, the code contains two errors. Try to find and fix the errors.

for item in ["sandals", "glasses", "trousers"):
    print(item.capitalize)

solution: close with ] and add () after capitalize

Coding Exercise 1
Create a program that:

1. Prompts the user to input a (dollar) amount.

2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.

3. Prints out the amount in euros, as shown in the screenshot below.

How many dollars have you got? 100
The amount in euros is:
95.0

dollars = float(input("How many dollars have you got?"))
print("The amount in euros is: " )
print(0.95*dollars)



Coding Exercise 2
The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.

ranking = ['John', 'Sen', 'Lisa']

Create a program that:

1. Contains the above list.

2. Prompts the user to input a rank number.

3. Returns the person who has the given rank.

For example:
Enter the rank number: 2
Sen

ranking = ['John', 'Sen', 'Lisa']
rank = int(input("Enter the rank number: "))
print(ranking[rank-1])


Coding Exercise 3
We have the same list:
ranking = ['John', 'Sen', 'Lisa']
This time you need to create a program that:
1. Contains the above list.
2 Prompts the user to input the person's name.
3. Returns the rank that person has.
For example:
Enter a name: Sen
2

ranking = ['John', 'Sen', 'Lisa']
name = input("Enter a name: ")
name.strip()

print(ranking.index(name)+1)

Bug-Fixing Exercise 1
The programmer is trying to extract and print out 'b' using list indexing, but there is an error. Try to fix it.

elements = ['a', 'b', 'c']
print(elements(1))

solution: add [] between 1


Bug-Fixing Exercise 2
The code below aims to replace 'b' with 'x' in the list elements.
However, the output of the code is still ['a', 'b', 'c'].
Try to fix the code so 'b' is replaced with 'x'.

elements = ['a', 'b', 'c']
new = 'x'
new = elements[1]
print(elements)

solution: invert order -->  elements[1] = new
elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
print(elements)

for i, item in enumerate(a):
    print(i, item)
enumerate returns a tuple with (index, element); the tuple can be displayed converting it to a list: list(enumerate(a))

fstring can combine int or float between quotes
f"{index}fdsfdsf{int}"


Coding Exercise 1
filenames = ['document', 'report', 'presentation']

Copy-paste the above list in a .py file and extend the code, so it prints out the output below:

0-Document.txt
1-Report.txt
2-Presentation.txt

filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    item = item.capitalize()
    print(f"{index}-{item}.txt")

    or
for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")


Coding Exercise 2
ips = ['100.122.133.105', '100.122.133.111']

Copy-paste the ips list in a .py file and extend the program so it:

1. Prompts the user to input an index (e.g, 0 or 1).

2. Returns the IP address that has that index.

Here is how the program would behave when executed:
Enter the index of the IP you want:1
You chose 100.122.133.111

ips = ['100.122.133.105', '100.122.133.111']

a = int(input("Enter the index of the IP you want:"))
print("You chose ", float(ips[a]))

or:
ips = ['100.122.133.105', '100.122.133.111']

user_choice = int(input("Enter the index of the IP you want: "))
message = f"You chose {ips[user_choice]}"
print(message)

Bug-Fixing Exercise 1
Supposedly, the following program should:

1. Prompt the user to input an index (e.g., 0, 1, or 2).

2. Print out the item with that index.

However, there is a bug with the program which you should try to fix.



menu = ["pasta", "pizza", "salad"]

user_choice = input("Enter the index of the item: ")

message = f"You chose {menu[user_choice]}."
print(message)

solution:
user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."


Here is another piece of buggy code:

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate[menu]:
    print(f"{i}.{j}")
Fix the code, so it prints out the output below:

0.pasta
1.pizza
2.salad

solution:
for i, j in enumerate(menu):


Bug-Fixing Exercise 3
Here is another piece of code that contains a bug:

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print("f{i}.{j}")
The expected output is this:

0.pasta
1.pizza
2.salad
Fix the bug so the program prints out the above output.
solution:     print(f"{i}.{j}")


Coding Exercise 1
Please download the essay.txt file from the resources of this article. Then, create a program that reads that file and prints out its text.
The first letter of each word in the output should be uppercase.

file=open(f"Day6/essay.txt",'r')
print(file.read().title())
file.close()

or
file = open("essay.txt", 'r')
content = file.read()
print(content.title())

Coding Exercise 2
Write a program that reads the essay.txt file and returns the number of characters contained in the file.
file=open(f"Day6/essay.txt",'r')
print(len(file.read()))
file.close()



Bug-Fixing Exercise 1: Take a look at the code below:

file = open("data.txt", 'w')

file.write("100.12")
file.write("111.23")

file.close()
The code creates a text file which contains the following content:

100.12111.23

However, the correct content should be:

100.12

111.23

Please fix the code so it creates the file with the correct content.

Solution
file = open("data.txt", 'w')

file.write("100.12")
file.write("111.23")

file.close()



Bug-Fixing Exercise 2: The code below tries to write the string "100.2" to the text file. However, there is an error. Try to fix the error.

file = open("data.txt", 'r')
file.write("100.12")
file.close()

solution
file = open("data.txt", 'w')
file.write("100.12")
file.close()

Coding Exercise 1
names = ["john smith", "jay santi", "eva kuki"]

Extend the code above so the code capitalizes all the names and surnames of the list and then prints the new list.

The output of your code should be as below:

['John Smith', 'Jay Santi', 'Eva Kuki']

solution:
new = [item.title() for item in names]
print(new)


Coding Exercise 2
usernames = ["john 1990", "alberta1970", "magnola2000"]

Extend the code above so the code prints out a list containing the number of characters for each username.

The output of your code should be as below:

[9, 11, 11]

solution:
length = [len(item) for item in usernames]
print(length)

Coding Exercise 3
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out a list containing the same items as floats.

The output of your code should be as below:

[10.0, 19.1, 20.0]

solution:
user_entries = ['10', '19.1', '20']
new = [float(item) for item in user_entries]
print(new)

Coding Exercise 4
user_entries = ['10', '19.1', '20']
Extend the code above so the code prints out the sum of the numbers.

The output of your code should be as below:

49.1
Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all numbers. For more info, try help(sum).

solution:
user_entries = ['10', '19.1', '20']
new = [float(item) for item in user_entries]
print(sum(new))

Bug-Fixing Exercise 1
The code below tries to write the items of temperatures each in one line in the file.txt list. However, the code has an error. Try to fix the error.

temperatures = [10, 12, 14]

file = open("file.txt", 'w')

file.writelines(temperatures)

solution:
declare temperatures=[str(item)+'\n' for item in temperatures]

Bug-Fixing Exercise 2
The code below tries to convert all the numbers to integers. However, the code has an error. Try to fix the error.

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for item in numbers]
print(numbers)

solution:
change line to numbers = [int(item) for item in numbers]

Coding exercise 1
Note: This is a very challenging exercise. Do not worry if you can't get it right. Just try to code until you get bored. The sole experience of trying to code helps your learning a ton.

A client wants to buy a coin-flip probability program from you.

The programs should work like this:

1. The user runs the program. The program asks the user to enter "head" or "tail".  The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail". The user does the same over and over again.
Throw the coin and enter head or tail here: ? tail
Heads: 0.0%
Throw the coin and enter head or tail here: ? head
Heads: 50.0%
Throw the coin and enter head or tail here: ? head
Heads: 66.6666666666%
Throw the coin and enter head or tail here: ? tail
Heads: 50.0%
Throw the coin and enter head or tail here:?

In each cycle, the program should return the current percentage of heads in the program, similar to what you see in the screenshot above. Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.
solution
head = 0
tail = 0
results = []
while True:
    result = input('Throw the coin and enter head or tail here: ?')
    result = result.strip().capitalize()
    results.append(result)
    with open("sides.txt", 'w') as file:
        for a in results:
            file.write(a + '\n')
    match result:
        case 'Head':
            head = head + 1
        case 'Tail':
            tail = tail + 1
    print(f"Heads: {float(head/(head+tail))*100}%")

or:
while True:
    with open("sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"

    sides.append(side)

    with open("sides.txt", 'w') as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    percentage = nr_heads / len(sides) * 100

    print(f"Heads: {percentage}%")


Bug-Fixing Exercise 1
with open("file.txt", 'r') as file:
    print(file.read())
    print(len(file.read()))
The Python script above is in the same directory with a file named file.txt whose content is:

Hello You

The Python script should print out the content of the file and the number of characters of the text inside file.txt. So, the expected output would be:

Hello You
9
However, the script prints out this:

Hello You
0
Can you fix the program so it prints out the expected output?
solution
with open("file.txt", 'r') as file:
    content = file.read()
print(content)
print(len(content))

'''
