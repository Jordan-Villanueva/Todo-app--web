# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
'''
def converter(vol_local):
    vol_lit = vol_local /1000
    return vol_lit


volume_liters = float(input('Enter your volume in liters: '))
print(f"Your volume in cubic meters is {converter(volume_liters)}")


Coding Exercise 2
Create a script that asks the user to enter a password. Then create a function that checks the
strength of the user password. The function should return Strong Password if all of the
following conditions are true:

Eight or more characters

At least one uppercase letter.

At least one digit.

Here is what happens when the user provides a password that satisfies all three conditions:
Enter new password: hello123HI
Strong password

And if the user enters a password that breaks one of the three conditions,
the program returns Weak Password:
Enter new password: hello
Weak password

Solution:
password = input("Enter new password: ")

def chec_password(password_loc):
    result = {}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True

    result["upper-case"] = uppercase

    if all(result.values()):
        print("Strong Password")
    else:
        print("Weak Password")

print(chec_password(password_glob))


'''
