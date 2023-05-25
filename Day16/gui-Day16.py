import PySimpleGUI as sp

label = sp.Text("Type in a to do")
input_box = sp.InputText(tooltip="Enter todo")
add_button = sp.Button("Add")

# Do not add only one list; at least add two elements list type inside layout to avoid errors
window = sp.Window('My To Do App', layout=[[label], [input_box, add_button]])
window.read()
print('Hello')
window.close()