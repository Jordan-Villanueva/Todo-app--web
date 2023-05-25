import PySimpleGUI as sp
from zip_creator_Day_17 import make_archive

label1 = sp.Text("Select files to compress:")
input1 = sp.Input()
choose_button1 = sp.FilesBrowse("Choose",key="files")

label2 = sp.Text("Select destination folder:")
input2 = sp.Input()
choose_button2 = sp.FolderBrowse("Choose",key="folder")

compress_button = sp.Button("Compress")
output_label = sp.Text(key="output", text_color="green")

window = sp.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!")

window.close()