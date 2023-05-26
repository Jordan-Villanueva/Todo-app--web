import PySimpleGUI as sp
from zip_extractor import extract_archive

sp.theme("Black")

label1 = sp.Text("Select archive:")
input1 = sp.Input()
choose_button1 = sp.FileBrowse("Choose", key="archive")

label2 = sp.Text("Select dest dir:")
input2 = sp.Input()
choose_button2 = sp.FolderBrowse("Choose", key="folder")

extract_button = sp.Button("Extract")
output_label = sp.Text(key="output", text_color="green")

window = sp.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()