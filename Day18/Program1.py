import PySimpleGUI as sp
import functions
import time

sp.theme("DarkPurple5")

clock = sp.Text("", key="clock")
label = sp.Text("Type in a to do")
input_box = sp.InputText(tooltip="Enter todo", key='todo')
add_button = sp.Button("Add", size=10)
list_box = sp.Listbox(values=functions.get_todos(), key='todos_list',
                      enable_events=True, size=[45, 10])
edit_button = sp.Button("Edit")
complete_button = sp.Button("Complete")
exit_button = sp.Button("Exit")

button_labels = ["Close", "Apply"]

'''
To create button instances
layout = []
for bl in button_labels:
    layout.append([sp.Button(bl)])
'''

layout = [[clock],[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
# Do not add only one list; at  least add two elements list type inside layout to avoid errors
window = sp.Window('My To Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(1, event)
    # print(2, values)
    # print(3, values['todos_list'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos_list'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
            except IndexError:
                sp.popup("Please select an item first", font=("Helvetica",20) )
        case "Complete":
            try:
                todo_to_complete = values['todos_list'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos_list'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sp.popup("Please select an item first", font=("Helvetica",20) )
        case "Exit":
            break
        case 'todos_list':
            window['todo'].update(value=values['todos_list'][0])
        case sp.WIN_CLOSED:
            break
            # exit() use to terminate the program

print("Bye")
window.close()