import PySimpleGUI as sp

import functions

label = sp.Text("Type in a to do")
input_box = sp.InputText(tooltip="Enter todo", key='todo')
add_button = sp.Button("Add")
list_box = sp.Listbox(values=functions.get_todos(), key='todos_list',
                      enable_events=True, size=[45, 10])
edit_button = sp.Button("Edit")

# Do not add only one list; at least add two elements list type inside layout to avoid errors
window = sp.Window('My To Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos_list'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos_list'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case 'todos_list':
            window['todo'].update(value=values['todos_list'][0])
        case sp.WIN_CLOSED:
            break

window.close()