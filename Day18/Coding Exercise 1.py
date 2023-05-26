"""
Coding Exercise 1
Your task for this exercise is to add an Exit button
 that quits the program and apply a black theme to the
 program you built-in yesterday's coding exercise.

import PySimpleGUI as sp
import functions

sp.theme("Black")

label1 = sp.Text("Enter feet:")
input1 = sp.Input(key="feet")

label2 = sp.Text("Enter inches:")
input2 = sp.Input(key="inches")

compress_button = sp.Button("Convert")
exit_button = sp.Button("Exit")
output_label = sp.Text(key="output")

window = sp.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [compress_button, exit_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    if event == 'Exit':
        break
    if event == sp.WIN_CLOSED:
        break
    else:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = functions.convert_to_meters(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white" )

window.close()

or

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")

"""