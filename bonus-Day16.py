import PySimpleGUI as sp

label1 = sp.Text("Select files to compress:")
input1 = sp.Input()
choose_button1 = sp.FileBrowse("Choose")

label2 = sp.Text("Select destination folder:")
input2 = sp.Input()
choose_button2 = sp.FolderBrowse("Choose")

compress_button = sp.Button("Compress")

window = sp.Window("File Compressor", layout=[[label1, input1, choose_button1], [label2, input2, choose_button2]])

window.read()
window.close()

'''
Coding exercise 1

import PySimpleGUI as sp
label1 = sp.Text("Enter feet:")
input1 = sp.Input()
label2 = sp.Text("Enter inches:")
input2 = sp.Input()
convert_button = sp.Button("Convert")

window = sp.Window("Convertor", layout=[[label1, input1], [label2, input2], [convert_button]])
window.read()
window.close()

Bug-Fixing Exercise 1


import PySimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
 
window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1, option2, option3, option4],
                           ])
 
window.read()
window.close()

Change the script so that the output is generated instead. 

Solution:

import PySimpleGUI as sg
 
label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")
 
window = sg.Window("File Compressor",
                   layout=[[label],
                           [option1], [option2], [option3], [option4],
                           ])
 
window.read()
window.close()


'''