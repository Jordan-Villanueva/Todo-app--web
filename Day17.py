import PySimpleGUI as sp

import functions

label = sp.Text("Type in a to do")
input_box = sp.InputText(tooltip="Enter todo", key='todo')
add_button = sp.Button("Add")

# Do not add only one list; at least add two elements list type inside layout to avoid errors
window = sp.Window('My To Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sp.WIN_CLOSED:
            break

window.close()