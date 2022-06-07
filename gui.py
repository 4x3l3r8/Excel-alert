import PySimpleGUI as sg
from shutil import copyfile
import os


def copy_file():
    sg.theme("black")
    layout = [
        [sg.T("")],
        [sg.Text("Choose a file: "), sg.Input(key="-In-"), sg.FileBrowse(key="-file-")],
        [sg.Ok("Submit"), sg.Cancel()],
    ]

    ###Building Window
    window = sg.Window("My File Browser", layout, size=(600, 150))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "Cancel"
        ):  # if user closes window or clicks cancel
            return "cancel"
        elif event == "Submit":
            print(values["-file-"])
            source = rf'{values["-file-"]}'
            destination = f"{os.getcwd()}\data\{os.path.basename(source)}"
            try:
                copyfile(source, destination)
                # print(f'Current working directory: {getcwd()}')
                print("File copied successfully.")
                return destination
            except Exception as e:
                print("Failed to copy file. Error: %s" % e)
                sg.popup_error_with_traceback(
                    f"An error happened.  Here is the info:", e
                )
                return False
        else:
            break
