import PySimpleGUI as sg
from shutil import copyfile
import os

sg.theme("white")
def copy_file():
    
    layout_to_center = [
        [sg.Text("Choose a file: "), sg.Input(key="-In-"), sg.FileBrowse(key="-file-")],
        [sg.Ok("Submit"), sg.Cancel()],
    ]

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(layout_to_center, element_justification="c"), sg.Push()],
        [sg.VPush()],
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
            username = os.getlogin()
            getWD=rf"C:\Users\{username}\Desktop\data"
            source = rf'{values["-file-"]}'
            destination = f"{getWD}\{os.path.basename(source)}"
            try:
                copyfile(source, destination)
                # print(f'Current working directory: {getcwd()}')
                print("File copied successfully.")
                # return destination
                return source
            except Exception as e:
                print("Failed to copy file. Error: %s" % e)
                sg.popup_error_with_traceback(
                    f"An error happened.  Here is the info:", e
                )
                return False
        else:
            break


def notify(msg):
    # sg.theme("black")
    layout_to_center = [
        [sg.T("")],
        [sg.Text(msg)],
        [sg.Ok("Ok", size=(10, 1))],
    ]
    
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Column(layout_to_center, element_justification="c"), sg.Push()],
        [sg.VPush()],
    ]

    ###Building Window
    window = sg.Window("Notification", layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if (
            event == sg.WIN_CLOSED or event == "Ok"
        ):  # if user closes window or clicks cancel
            break
        else:
            break
