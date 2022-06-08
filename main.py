import gui
import pandas as pd
import os
import sys
from datetime import *

if not os.path.exists(f"{os.getcwd()}\data"):
    os.mkdir(f"{os.getcwd()}\data")
    file_found = False
    file = gui.copy_file()
else:
    file_found = True
    file = open(f"{os.getcwd()}\data\path_to_file.txt", "r").read().split()[0]
    # print(file)

# file = gui.copy_file()
if file != "cancel" and file != False:
    print("file in dir: ", file)
    if file_found == False:
        with open(f"{os.getcwd()}\data\path_to_file.txt", "w") as f:
            f.write(f"{file} \n")
            f.close()

    # === === === === Extract data from file into dataframe === === === ===
    data = pd.read_excel(file)
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
        Notification_text = f"{row['Description']} and {len(unpaid_persons_expiry_date_df) - 1} others are due for payment since {row['Due Date']}\n"
        
    # Fire notification
    gui.notify(Notification_text)