import PySimpleGUI as sg
import gui
import pandas as pd
import os

# import xlrd
import sys
from datetime import *


def MainRun():
    try:
        username = os.getlogin()
        getWD = rf"C:\Users\{username}\Desktop\data"

        if not os.path.isfile(f"{getWD}\path_to_file.txt"):
            if not os.path.exists(getWD):
                os.mkdir(getWD)
            file_found = False
            file = gui.copy_file()
        else:
            file_found = True
            file = open(f"{getWD}\path_to_file.txt", "r").read().split()[0]
            # print(file)

        # file = gui.copy_file()
        if file != "cancel" and file != False:
            print("file in dir: ", file)
            if file_found == False:
                with open(f"{getWD}\path_to_file.txt", "w") as f:
                    f.write(f"{file} \n")
                    f.close()

            # === === === === Extract data from file into dataframe === === === ===
            data = pd.read_excel(file, engine="openpyxl")
            df = pd.DataFrame(data)

            # initialise unpaid persons array
            unpaid_persons = []

            # === === === === Get Unpaid People === === === ===
            for i in range(len(df)):
                if df.loc[i, "Paid"] == False:
                    unpaid_persons.append(df.loc[i])
    
            # initialise unpaid persons expiry dates array
            unpaid_persons_expiry_date = []

            # === === === === from unpaid people, get Due date=== === === ===
            unpaid_persons_df = pd.DataFrame(unpaid_persons)
            for index, row in unpaid_persons_df.iterrows():
                if row["Due Date"] <= datetime.now():
                    unpaid_persons_expiry_date.append(row)

            unpaid_persons_expiry_date_df = pd.DataFrame(unpaid_persons_expiry_date)

            # === === === === Trigger Notification based on results === === === ===
            Notification_text = ""

            for index, row in unpaid_persons_expiry_date_df.iterrows():
                Notification_text = f"{row['Name']} and {len(unpaid_persons_expiry_date_df) - 1} others have been due for payment since {row['Due Date'].strftime('%a, %d-%b-%Y')}\n"

            # Fire notification
            gui.notify(Notification_text)
    except Exception as e:
        print("An Error Occured. Error: %s" % e)
        sg.popup_error(
            f"An error occurred!. Error: {e}", title="Error", no_titlebar=True
        )


MainRun()