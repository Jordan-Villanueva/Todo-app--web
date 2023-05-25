import PySimpleGUI as sp
import functions


label1 = sp.Text("Enter feet:")
input1 = sp.Input(key="feet")

label2 = sp.Text("Enter inches:")
input2 = sp.Input(key="inches")

compress_button = sp.Button("Convert")
output_label = sp.Text(key="output")

window = sp.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = functions.convert_to_meters(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white" )

window.close()